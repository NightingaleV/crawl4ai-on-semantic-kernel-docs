import asyncio
from crawl4ai import *
from crawl4ai import LLMExtractionStrategy, LLMConfig

START_PAGE = "https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?toc=/semantic-kernel/toc.json&pivots=programming-language-python"

# async def main():
USE_LLM_STRATEGY = False
LLM_API_TOKEN = ''

REMOVE_HEAD = 53 # Lines


async def crawl_website(website_url: str):
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )

    # Strategy to crawl the website
    keyword_scorer = KeywordRelevanceScorer(
        keywords=["concepts", "example", "python", "configuration", 'api'],
        weight=0.7  # Importance of this scorer (0.0 to 1.0)
    )

    filter_chain = FilterChain([
        URLPatternFilter(patterns=["*semantic-kernel*"]),
        DomainFilter(
            allowed_domains=["learn.microsoft.com"],
        ),
        ContentTypeFilter(allowed_types=["text/html"])
    ])

    crawl_strategy = BestFirstCrawlingStrategy(
        max_depth=1,
        include_external=False,
        url_scorer=keyword_scorer,
        max_pages=60,  # Maximum number of pages to crawl (optional)
        filter_chain=filter_chain,

    )

    extraction_strategy = LLMExtractionStrategy(
        llm_config=LLMConfig(provider="deepseek/deepseek-chat", api_token=LLM_API_TOKEN),
        # schema=MyModel.model_json_schema(),
        extraction_type="block",
        instruction="Extract the information regarding semantic-kernel library and its usage and documentation. "
                    "Make sure to include the concepts, pictures, examples, code snippets and configuration details. Remove all the code snippets for C# and Java, keep only python code examples."
                    "Output Raw but formatted Markdown Syntax. Don't include apart from the raw content no other descriptions regarding what you are doing and end notes.",
        apply_chunking=True,
        chunk_token_threshold=1000,
        # overlap_rate=0.1,
        input_format="markdown",
        extra_args={"temperature": 0.3},
        verbose=True
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        md_generator = DefaultMarkdownGenerator(
            options={
                "ignore_links": False,
                "escape_html": False,
                "body_width": 120
            },
        )

        crawl_config = CrawlerRunConfig(
            semaphore_count=10,
            css_selector='.mainContainer',
            extraction_strategy=extraction_strategy if USE_LLM_STRATEGY else None,
            deep_crawl_strategy=crawl_strategy,
            markdown_generator=md_generator,
            cache_mode=CacheMode.BYPASS,
            word_count_threshold=5,
            exclude_external_links=True,
            remove_overlay_elements=True,
            process_iframes=False,
            prettiify=True,
            page_timeout=30_000,
            excluded_tags=['form', 'header', 'footer'],
        )
        results = await crawler.arun(
            url=website_url,
            config=crawl_config,
            # dispatcher=dispatcher,
        )

        return results


results = asyncio.run(crawl_website(website_url=START_PAGE))

import pathlib

CONTENT_PATH = pathlib.Path('./data/docs')
CONTENT_PATH.mkdir(parents=True, exist_ok=True)
for i, result in enumerate(results):
    with open(CONTENT_PATH / f'semantic_kernel_docs_{i}.md', 'w', encoding='utf-8') as f:
        # remove 50 lines from the head
        f.write('\n'.join(result.markdown.split('\n')[REMOVE_HEAD:]))
