
#### Share via

Print

Table of contents

# Using plugins for Retrieval Augmented Generation (RAG)

  * Article
  * 06/24/2024
  * 2 contributors

Feedback

## In this article

  1. [Semantic vs classic search](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#semantic-vs-classic-search)
  2. [Dynamic vs pre-fetched data retrieval](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#dynamic-vs-pre-fetched-data-retrieval)
  3. [Keeping data secure](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#keeping-data-secure)
  4. [Next steps](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#next-steps)

Often, your AI agents must retrieve data from external sources to generate grounded responses. Without this additional
context, your AI agents may hallucinate or provide incorrect information. To address this, you can use plugins to
retrieve data from external sources.

When considering plugins for Retrieval Augmented Generation (RAG), you should ask yourself two questions:

  1. How will you (or your AI agent) "search" for the required data? Do you need [semantic search](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#semantic-search) or [classic search](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#classic-search)?
  2. Do you already know the data the AI agent needs ahead of time ([pre-fetched data](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#pre-fetched-data-retrieval)), or does the AI agent need to retrieve the data [dynamically](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#dynamic-data-retrieval)?
  3. How will you keep your data secure and [prevent oversharing of sensitive information](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#keeping-data-secure)?

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#semantic-
vs-classic-search)

## Semantic vs classic search

When developing plugins for Retrieval Augmented Generation (RAG), you can use two types of search: semantic search and
classic search.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#semantic-
search)

### Semantic Search

Semantic search utilizes vector databases to understand and retrieve information based on the meaning and context of the
query rather than just matching keywords. This method allows the search engine to grasp the nuances of language, such as
synonyms, related concepts, and the overall intent behind a query.

Semantic search excels in environments where user queries are complex, open-ended, or require a deeper understanding of
the content. For example, searching for "best smartphones for photography" would yield results that consider the context
of photography features in smartphones, rather than just matching the words "best," "smartphones," and "photography."

When providing an LLM with a semantic search function, you typically only need to define a function with a single search
query. The LLM will then use this function to retrieve the necessary information. Below is an example of a semantic
search function that uses Azure AI Search to find documents similar to a given query.

C# Copy

```

using System.ComponentModel;

using System.Text.Json.Serialization;

using Azure;

using Azure.Search.Documents;

using Azure.Search.Documents.Indexes;

using Azure.Search.Documents.Models;

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.Embeddings;

public class InternalDocumentsPlugin

{

  private readonly ITextEmbeddingGenerationService _textEmbeddingGenerationService;

  private readonly SearchIndexClient _indexClient;

  public AzureAISearchPlugin(ITextEmbeddingGenerationService textEmbeddingGenerationService, SearchIndexClient
indexClient)

  {

    _textEmbeddingGenerationService = textEmbeddingGenerationService;
    _indexClient = indexClient;
  }

  [KernelFunction("Search")]

  [Description("Search for a document similar to the given query.")]

  public async Task<string> SearchAsync(string query)

  {

    // Convert string query to vector
    ReadOnlyMemory<float> embedding = await _textEmbeddingGenerationService.GenerateEmbeddingAsync(query);
    // Get client for search operations
    SearchClient searchClient = _indexClient.GetSearchClient("default-collection");
    // Configure request parameters
    VectorizedQuery vectorQuery = new(embedding);
    vectorQuery.Fields.Add("vector");
    SearchOptions searchOptions = new() { VectorSearch = new() { Queries = { vectorQuery } } };
    // Perform search request
    Response<SearchResults<IndexSchema>> response = await searchClient.SearchAsync<IndexSchema>(searchOptions);
    // Collect search results
    await foreach (SearchResult<IndexSchema> result in response.Value.GetResultsAsync())
    {
      return result.Document.Chunk; // Return text from first result
    }
    return string.Empty;
  }

  private sealed class IndexSchema

  {

    [JsonPropertyName("chunk")]
    public string Chunk { get; set; }
    [JsonPropertyName("vector")]
    public ReadOnlyMemory<float> Vector { get; set; }
  }

}

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#classic-
search)

### Classic Search

Classic search, also known as attribute-based or criteria-based search, relies on filtering and matching exact terms or
values within a dataset. It is particularly effective for database queries, inventory searches, and any situation where
filtering by specific attributes is necessary.

For example, if a user wants to find all orders placed by a particular customer ID or retrieve products within a
specific price range and category, classic search provides precise and reliable results. Classic search, however, is
limited by its inability to understand context or variations in language.

Tip

In most cases, your existing services already support classic search. Before implementing a semantic search, consider
whether your existing services can provide the necessary context for your AI agents.

Take for example, a plugin that retrieves customer information from a CRM system using classic search. Here, the AI
simply needs to call the `GetCustomerInfoAsync` function with a customer ID to retrieve the necessary information.

C# Copy

```

using System.ComponentModel;

using Microsoft.SemanticKernel;

public class CRMPlugin

{

  private readonly CRMService _crmService;

  public CRMPlugin(CRMService crmService)

  {

    _crmService = crmService;
  }

  [KernelFunction("GetCustomerInfo")]

  [Description("Retrieve customer information based on the given customer ID.")]

  public async Task<Customer> GetCustomerInfoAsync(string customerId)

  {

    return await _crmService.GetCustomerInfoAsync(customerId);
  }

}

```

Achieving the same search functionality with semantic search would likely be impossible or impractical due to the non-
deterministic nature of semantic queries.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#when-to-
use-each)

### When to Use Each

Choosing between semantic and classic search depends on the nature of the query. It is ideal for content-heavy
environments like knowledge bases and customer support where users might ask questions or look for products using
natural language. Classic search, on the other hand, should be employed when precision and exact matches are important.

In some scenarios, you may need to combine both approaches to provide comprehensive search capabilities. For instance, a
chatbot assisting customers in an e-commerce store might use semantic search to understand user queries and classic
search to filter products based on specific attributes like price, brand, or availability.

Below is an example of a plugin that combines semantic and classic search to retrieve product information from an
e-commerce database.

C# Copy

```

using System.ComponentModel;

using Microsoft.SemanticKernel;

public class ECommercePlugin

{

  [KernelFunction("search_products")]

  [Description("Search for products based on the given query.")]

  public async Task<IEnumerable<Product>> SearchProductsAsync(string query, ProductCategories category = null, decimal?
minPrice = null, decimal? maxPrice = null)

  {

    // Perform semantic and classic search with the given parameters
  }

}

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#dynamic-vs-
pre-fetched-data-retrieval)

## Dynamic vs pre-fetched data retrieval

When developing plugins for Retrieval Augmented Generation (RAG), you must also consider whether the data retrieval
process is static or dynamic. This allows you to optimize the performance of your AI agents by retrieving data only when
necessary.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#dynamic-
data-retrieval)

### Dynamic data retrieval

In most cases, the user query will determine the data that the AI agent needs to retrieve. For example, a user might ask
for the difference between two different products. The AI agent would then need to dynamically retrieve the product
information from a database or API to generate a response using [function calling](https://learn.microsoft.com/en-
us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/). It would be impractical to pre-fetch all
possible product information ahead of time and give it to the AI agent.

Below is an example of a back-and-forth chat between a user and an AI agent where dynamic data retrieval is necessary.

Expand table

Role | Message  
---|---  
🔵 **User** | Can you tell me about the best mattresses?  
🔴 **Assistant (function call)** | `Products.Search("mattresses")`  
🟢 **Tool** | `[{"id": 25323, "name": "Cloud Nine"},{"id": 63633, "name": "Best Sleep"}]`  
🔴 **Assistant** | Sure! We have both Cloud Nine and Best Sleep  
🔵 **User** | What's the difference between them?  
🔴 **Assistant (function call)** | `Products.GetDetails(25323)` `Products.GetDetails(63633)`  
🟢 **Tool** | `{ "id": 25323, "name": "Cloud Nine", "price": 1000, "material": "Memory foam" }`  
🟢 **Tool** | `{ "id": 63633, "name": "Best Sleep", "price": 1200, "material": "Latex" }`  
🔴 **Assistant** | Cloud Nine is made of memory foam and costs $1000. Best Sleep is made of latex and costs $1200.  
[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#pre-
fetched-data-retrieval)

### Pre-fetched data Retrieval

Static data retrieval involves fetching data from external sources and _always_ providing it to the AI agent. This is
useful when the data is required for every request or when the data is relatively stable and doesn't change frequently.

Take for example, an agent that always answers questions about the local weather. Assuming you have a `WeatherPlugin`,
you can pre-fetch weather data from a weather API and provide it in the chat history. This allows the agent to generate
responses about the weather without wasting time requesting the data from the API.

C# Copy

```

using System.Text.Json;

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.ChatCompletion;

IKernelBuilder builder = Kernel.CreateBuilder();

builder.AddAzureOpenAIChatCompletion(deploymentName, endpoint, apiKey);

builder.Plugins.AddFromType<WeatherPlugin>();

Kernel kernel = builder.Build();

// Get the weather

var weather = await kernel.Plugins.GetFunction("WeatherPlugin", "get_weather").InvokeAsync(kernel);

// Initialize the chat history with the weather

ChatHistory chatHistory = new ChatHistory("The weather is:\n" + JsonSerializer.Serialize(weather));

// Simulate a user message

chatHistory.AddUserMessage("What is the weather like today?");

// Get the answer from the AI agent

IChatCompletionService chatCompletionService = kernel.GetRequiredService<IChatCompletionService>();

var result = await chatCompletionService.GetChatMessageContentAsync(chatHistory);

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#keeping-
data-secure)

## Keeping data secure

When retrieving data from external sources, it is important to ensure that the data is secure and that sensitive
information is not exposed. To prevent oversharing of sensitive information, you can use the following strategies:

Expand table

Strategy | Description  
---|---  
**Use the user's auth token** | Avoid creating service principals used by the AI agent to retrieve information for users. Doing so makes it difficult to verify that a user has access to the retrieved information.  
**Avoid recreating search services** | Before creating a new search service with a vector DB, check if one already exists for the service that has the required data. By reusing existing services, you can avoid duplicating sensitive content, leverage existing access controls, and use existing filtering mechanisms that only return data the user has access to.  
**Store reference in vector DBs instead of content** | Instead of duplicating sensitive content to vector DBs, you can store references to the actual data. For a user to access this information, their auth token must first be used to retrieve the real data.  
[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag#next-steps)

## Next steps

Now that you now how to ground your AI agents with data from external sources, you can now learn how to use AI agents to
automate business processes. To learn more, see [using task automation functions](https://learn.microsoft.com/en-
us/semantic-kernel/concepts/plugins/using-task-automation-functions).

[Learn about task automation functions](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-
automation-functions)

## Additional resources

Documentation

  * [ Give agents access to OpenAPI APIs ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?source=recommendations)
Learn how to add plugins from OpenAPI specifications to your agents in Semantic Kernel.

  * [ Provide native code to your agents ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-native-plugins?source=recommendations)
Learn how to add and invoke native code as plugins in Semantic Kernel.

  * [ What are Planners in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning?source=recommendations)
Learn what a planner is in Semantic Kernel.

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

  * [ Give agents access to Logic Apps via plugins ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-logic-apps-as-plugins?source=recommendations)
Provide your workflows to agents in Semantic Kernel by adding them as plugins.

  * [ Allow agents to automate tasks ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions?source=recommendations)
Learn how you safely allow agents to automate tasks on behalf of users in Semantic Kernel.

  * [ Text Search with Semantic Kernel (Preview) ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/text-search/?source=recommendations)
Describes what a Semantic Kernel Text Search is, an provides a basic example of how to use one and how to get started.

  * [ Semantic Kernel Text Search Plugins (Preview) ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/text-search/text-search-plugins?source=recommendations)
Describes how to create and use Semantic Kernel text search plugins. Includes samples showing how to use filters and how
to create a custom search plugin.

Show 5 more

Training

Module

[ Build a RAG-based agent with your own data using Azure AI Foundry - Training ](https://learn.microsoft.com/en-
us/training/modules/build-copilot-ai-studio/?source=recommendations)

Agents can work alongside you to provide suggestions, generate content, or help you make decisions. Agents use language
models as a form of generative artificial intelligence (AI) and will answer your questions using the data they were
trained on. To ensure an agent retrieves information from a specific source, you can add your own data when building an
agent with the Azure AI Foundry.

Certification

[ Microsoft Certified: Azure AI Engineer Associate - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-engineer/?source=recommendations)

Design and implement an Azure AI solution using Azure AI services, Azure AI Search, and Azure Open AI.

## Additional resources

Training

Module

[ Build a RAG-based agent with your own data using Azure AI Foundry - Training ](https://learn.microsoft.com/en-
us/training/modules/build-copilot-ai-studio/?source=recommendations)

Agents can work alongside you to provide suggestions, generate content, or help you make decisions. Agents use language
models as a form of generative artificial intelligence (AI) and will answer your questions using the data they were
trained on. To ensure an agent retrieves information from a specific source, you can add your own data when building an
agent with the Azure AI Foundry.

Certification

[ Microsoft Certified: Azure AI Engineer Associate - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-engineer/?source=recommendations)

Design and implement an Azure AI solution using Azure AI services, Azure AI Search, and Azure Open AI.

Documentation

  * [ Give agents access to OpenAPI APIs ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?source=recommendations)
Learn how to add plugins from OpenAPI specifications to your agents in Semantic Kernel.

  * [ Provide native code to your agents ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-native-plugins?source=recommendations)
Learn how to add and invoke native code as plugins in Semantic Kernel.

  * [ What are Planners in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning?source=recommendations)
Learn what a planner is in Semantic Kernel.

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

  * [ Give agents access to Logic Apps via plugins ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-logic-apps-as-plugins?source=recommendations)
Provide your workflows to agents in Semantic Kernel by adding them as plugins.

  * [ Allow agents to automate tasks ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions?source=recommendations)
Learn how you safely allow agents to automate tasks on behalf of users in Semantic Kernel.

  * [ Text Search with Semantic Kernel (Preview) ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/text-search/?source=recommendations)
Describes what a Semantic Kernel Text Search is, an provides a basic example of how to use one and how to get started.

  * [ Semantic Kernel Text Search Plugins (Preview) ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/text-search/text-search-plugins?source=recommendations)
Describes how to create and use Semantic Kernel text search plugins. Includes samples showing how to use filters and how
to create a custom search plugin.

Show 5 more

### In this article

