
# Supported Semantic Kernel languages

  * Article
  * 11/11/2024
  * 10 contributors

Feedback

## In this article

  1. [C# packages](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#c-packages)
  2. [Available features in each SDK](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#available-features-in-each-sdk)

Semantic Kernel plans on providing support to the following languages:

  * C#
  * Python
  * Java

While the overall architecture of the kernel is consistent across all languages, we made sure the SDK for each language
follows common paradigms and styles in each language to make it feel native and easy to use.

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#c-packages)

## C# packages

In C#, there are several packages to help ensure that you only need to import the functionality that you need for your
project. The following table shows the available packages in C#.

Expand table

Package name | Description  
---|---  
`Microsoft.SemanticKernel` | The main package that includes everything to get started  
`Microsoft.SemanticKernel.Core` | The core package that provides implementations for `Microsoft.SemanticKernel.Abstractions`  
`Microsoft.SemanticKernel.Abstractions` | The base abstractions for Semantic Kernel  
`Microsoft.SemanticKernel.Connectors.Amazon` | The AI connector for Amazon AI  
`Microsoft.SemanticKernel.Connectors.AzureAIInference` | The AI connector for Azure AI Inference  
`Microsoft.SemanticKernel.Connectors.AzureOpenAI` | The AI connector for Azure OpenAI  
`Microsoft.SemanticKernel.Connectors.Google` | The AI connector for Google models (e.g., Gemini)  
`Microsoft.SemanticKernel.Connectors.HuggingFace` | The AI connector for Hugging Face models  
`Microsoft.SemanticKernel.Connectors.MistralAI` | The AI connector for Mistral AI models  
`Microsoft.SemanticKernel.Connectors.Ollama` | The AI connector for Ollama  
`Microsoft.SemanticKernel.Connectors.Onnx` | The AI connector for Onnx  
`Microsoft.SemanticKernel.Connectors.OpenAI` | The AI connector for OpenAI  
`Microsoft.SemanticKernel.Connectors.AzureAISearch` | The vector store connector for AzureAISearch  
`Microsoft.SemanticKernel.Connectors.AzureCosmosDBMongoDB` | The vector store connector for AzureCosmosDBMongoDB  
`Microsoft.SemanticKernel.Connectors.AzureCosmosDBNoSQL` | The vector store connector for AzureAISearch  
`Microsoft.SemanticKernel.Connectors.MongoDB` | The vector store connector for MongoDB  
`Microsoft.SemanticKernel.Connectors.Pinecone` | The vector store connector for Pinecone  
`Microsoft.SemanticKernel.Connectors.Qdrant` | The vector store connector for Qdrant  
`Microsoft.SemanticKernel.Connectors.Redis` | The vector store connector for Redis  
`Microsoft.SemanticKernel.Connectors.Sqlite` | The vector store connector for Sqlite  
`Microsoft.SemanticKernel.Connectors.Weaviate` | The vector store connector for Weaviate  
`Microsoft.SemanticKernel.Plugins.OpenApi` (Experimental) | Enables loading plugins from OpenAPI specifications  
`Microsoft.SemanticKernel.PromptTemplates.Handlebars` | Enables the use of Handlebars templates for prompts  
`Microsoft.SemanticKernel.Yaml` | Provides support for serializing prompts using YAML files  
`Microsoft.SemanticKernel.Prompty` | Provides support for serializing prompts using Prompty files  
`Microsoft.SemanticKernel.Agents.Abstractions` | Provides abstractions for creating agents  
`Microsoft.SemanticKernel.Agents.OpenAI` | Provides support for Assistant API agents  
To install any of these packages, you can use the following command:

Bash Copy

```

dotnet add package <package-name>

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#python-packages)

## Python packages

In Python, there's a single package that includes everything you need to get started with Semantic Kernel. To install
the package, you can use the following command:

Bash Copy

```

pip install semantic-kernel

```

On under `Provides-Extra` the additional extras you can install are also listed and when used that will install the
packages needed for using SK with that specific connector or service, you can install those with the square bracket
syntax for instance:

Bash Copy

```

pip install semantic-kernel[azure]

```

This will install Semantic Kernel, as well as specific tested versions of: `azure-ai-inference`, `azure-search-
documents`, `azure-core`, `azure-identity`, `azure-cosmos` and `msgraph-sdk` (and any dependencies of those packages).
Similarly the extra `hugging_face` will install `transformers` and `sentence-transformers`.

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#java-packages)

## Java packages

For Java, Semantic Kernel has the following packages; all are under the group Id `com.microsoft.semantic-kernel`, and
can be imported from maven.

XML Copy

```

  <dependency>

    <groupId>com.microsoft.semantic-kernel</groupId>
    <artifactId>semantickernel-api</artifactId>
  </dependency>

```

A BOM is provided that can be used to define the versions of all Semantic Kernel packages.

XML Copy

```

  <dependencyManagement>

    <dependencies>
      <dependency>
        <groupId>com.microsoft.semantic-kernel</groupId>
        <artifactId>semantickernel-bom</artifactId>
        <version>${semantickernel.version}</version>
        <scope>import</scope>
        <type>pom</type>
      </dependency>
    </dependencies>
  </dependencyManagement>

```

  * `semantickernel-bom` – A Maven project BOM that can be used to define the versions of all Semantic Kernel packages.
  * `semantickernel-api` – Package that defines the core public API for the Semantic Kernel for a Maven project.
  * `semantickernel-aiservices-openai` –Provides a connector that can be used to interact with the OpenAI API.

Below is an example POM XML for a simple project that uses OpenAI.

XML Copy

```

<project>

  <dependencyManagement>

    <dependencies>
      <dependency>
        <groupId>com.microsoft.semantic-kernel</groupId>
        <artifactId>semantickernel-bom</artifactId>
        <version>${semantickernel.version}</version>
        <scope>import</scope>
        <type>pom</type>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <dependencies>

    <dependency>
      <groupId>com.microsoft.semantic-kernel</groupId>
      <artifactId>semantickernel-api</artifactId>
    </dependency>
    <dependency>
      <groupId>com.microsoft.semantic-kernel</groupId>
      <artifactId>semantickernel-connectors-ai-openai</artifactId>
    </dependency>
  </dependencies>

</project>

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#available-features-in-each-sdk)

## Available features in each SDK

The following tables show which features are available in each language. The 🔄 symbol indicates that the feature is
partially implemented, please see the associated note column for more details. The ❌ symbol indicates that the feature
is not yet available in that language; if you would like to see a feature implemented in a language, please consider
[contributing to the project](https://learn.microsoft.com/en-us/semantic-kernel/get-started/contributing) or [opening an
issue](https://learn.microsoft.com/en-us/semantic-kernel/get-started/contributing#reporting-issues).

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#core-capabilities)

### Core capabilities

Expand table

Services | C# | Python | Java | Notes  
---|---|---|---|---  
Prompts | ✅ | ✅ | ✅ | To see the full list of supported template and serialization formats, refer to the tables below  
Native functions and plugins | ✅ | ✅ | ✅  
OpenAPI plugins | ✅ | ✅ | ✅ | Java has a sample demonstrating how to load OpenAPI plugins  
Automatic function calling | ✅ | ✅ | ✅  
Open Telemetry logs | ✅ | ✅ | ❌  
Hooks and filters | ✅ | ✅ | ✅  
[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#prompt-template-formats)

### Prompt template formats

When authoring prompts, Semantic Kernel provides a variety of template languages that allow you to embed variables and
invoke functions. The following table shows which template languages are supported in each language.

Expand table

Formats | C# | Python | Java | Notes  
---|---|---|---|---  
Semantic Kernel template language | ✅ | ✅ | ✅  
Handlebars | ✅ | ✅ | ✅  
Liquid | ✅ | ❌ | ❌  
Jinja2 | ❌ | ✅ | ❌  
[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#prompt-serialization-formats)

### Prompt serialization formats

Once you've created a prompt, you can serialize it so that it can be stored or shared across teams. The following table
shows which serialization formats are supported in each language.

Expand table

Formats | C# | Python | Java | Notes  
---|---|---|---|---  
YAML | ✅ | ✅ | ✅  
Prompty | ✅ | ❌ | ❌  
[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#ai-services-modalities)

### AI Services Modalities

Expand table

Services | C# | Python | Java | Notes  
---|---|---|---|---  
Text Generation | ✅ | ✅ | ✅ | Example: Text-Davinci-003  
Chat Completion | ✅ | ✅ | ✅ | Example: GPT4, Chat-GPT  
Text Embeddings (Experimental) | ✅ | ✅ | ✅ | Example: Text-Embeddings-Ada-002  
Text to Image (Experimental) | ✅ | ✅ | ❌ | Example: Dall-E  
Image to Text (Experimental) | ✅ | ❌ | ❌ | Example: Pix2Struct  
Text to Audio (Experimental) | ✅ | ✅ | ❌ | Example: Text-to-speech  
Audio to Text (Experimental) | ✅ | ✅ | ❌ | Example: Whisper  
[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#ai-service-connectors)

### AI Service Connectors

Expand table

Endpoints | C# | Python | Java | Notes  
---|---|---|---|---  
Amazon Bedrock | ✅ | ✅ | ❌  
Anthropic | ✅ | ✅ | ❌  
Azure AI Inference | ✅ | ✅ | ❌  
Azure OpenAI | ✅ | ✅ | ✅  
Google | ✅ | ✅ | ✅  
Hugging Face Inference API | ✅ | ✅ | ❌  
Mistral | ✅ | ✅ | ❌  
Ollama | ✅ | ✅ | ❌  
ONNX | ✅ | ✅ | ❌  
OpenAI | ✅ | ✅ | ✅  
Other endpoints that suppoprt OpenAI APIs | ✅ | ✅ | ✅ | Includes LLM Studio, etc.  
[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#vector-store-connectors-
experimental)

### Vector Store Connectors (Experimental)

Warning

The Semantic Kernel Vector Store functionality is in preview, and improvements that require breaking changes may still
occur in limited circumstances before release.

For the list of out of the box vector store connectors and the language support for each, refer to [out of the box
connectors](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/out-of-the-box-
connectors/).

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages#memory-store-connectors-legacy)

### Memory Store Connectors (Legacy)

Important

Memory Store connectors are legacy and have been replaced by Vector Store connectors. For more information see [Legacy
Memory Stores](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/memory-stores).

Expand table

Memory Connectors | C# | Python | Java | Notes  
---|---|---|---|---  
Azure AI Search | ✅ | ✅ | ✅  
Chroma | ✅ | ✅ | ❌  
DuckDB | ✅ | ❌ | ❌  
Milvus | ✅ | ✅ | ❌  
Pinecone | ✅ | ✅ | ❌  
Postgres | ✅ | ✅ | ❌  
Qdrant | ✅ | ✅ | ❌  
Redis | ✅ | ✅ | ❌  
Sqlite | ✅ | ❌ | 🔄  
Weaviate | ✅ | ✅ | ❌  
## Additional resources

## Additional resources

### In this article

