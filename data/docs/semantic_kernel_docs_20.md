
Table of contents[ Read in English ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-
completion/?tabs=csharp-AzureOpenAI%2Cpython-AzureOpenAI%2Cjava-AzureOpenAI#streaming-chat-completion "Read in English")
Add to Collections Add to plan

#### Share via

Print

Table of contents

# Chat completion

  * Article
  * 11/21/2024
  * 8 contributors

Feedback

## In this article

  1. [Setting up your local environment](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#setting-up-your-local-environment)
  2. [Installing the necessary packages](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#installing-the-necessary-packages)
  3. [Creating chat completion services](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#creating-chat-completion-services)
  4. [Retrieving chat completion services](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#retrieving-chat-completion-services)
  5. [Using chat completion services](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#using-chat-completion-services)
  6. [Next steps](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#next-steps)

Show 2 more

With chat completion, you can simulate a back-and-forth conversation with an AI agent. This is of course useful for
creating chat bots, but it can also be used for creating autonomous agents that can complete business processes,
generate code, and more. As the primary model type provided by OpenAI, Google, Mistral, Facebook, and others, chat
completion is the most common AI service that you will add to your Semantic Kernel project.

When picking out a chat completion model, you will need to consider the following:

  * What modalities does the model support (e.g., text, image, audio, etc.)?
  * Does it support function calling?
  * How fast does it receive and generate tokens?
  * How much does each token cost?

Important

Of all the above questions, the most important is whether the model supports function calling. If it does not, you will
not be able to use the model to call your existing code. Most of the latest models from OpenAI, Google, Mistral, and
Amazon all support function calling. Support from small language models, however, is still limited.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#setting-up-your-local-
environment)

## Setting up your local environment

Some of the AI Services can be hosted locally and may require some setup. Below are instructions for those that support
this.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-OpenAI)
  * [Mistral](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-Mistral)
  * [Google](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-Google)
  * [Hugging Face](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-HuggingFace)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-AzureAIInference)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-Ollama)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-AmazonBedrock)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-ONNX)
  * [Other](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_1_csharp-other)

No local setup.

No local setup.

No local setup.

No local setup.

No local setup.

No local setup.

To run Ollama locally using docker, use the following command to start a container using the CPU.

Bash Copy

```

docker run -d -v "c:\temp\ollama:/root/.ollama" -p 11434:11434 --name ollama ollama/ollama

```

To run Ollama locally using docker, use the following command to start a container using GPUs.

Bash Copy

```

docker run -d --gpus=all -v "c:\temp\ollama:/root/.ollama" -p 11434:11434 --name ollama ollama/ollama

```

After the container has started, launch a Terminal window for the docker container, e.g. if using docker desktop, choose
`Open in Terminal` from actions.

From this terminal download the required models, e.g. here we are downloading the phi3 model.

Bash Copy

```

ollama pull phi3

```

No local setup.

No local setup.

Clone the repository containing the ONNX model you would like to use.

Bash Copy

```

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

```

No local setup.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#installing-the-necessary-
packages)

## Installing the necessary packages

Before adding chat completion to your kernel, you will need to install the necessary packages. Below are the packages
you will need to install for each AI service provider.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-OpenAI)
  * [Mistral](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-Mistral)
  * [Google](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-Google)
  * [Hugging Face](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-HuggingFace)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-AzureAIInference)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-Ollama)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-AmazonBedrock)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-ONNX)
  * [Other](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_2_csharp-other)

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.AzureOpenAI

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.OpenAI

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.MistralAI --prerelease

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.Google --prerelease

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.HuggingFace --prerelease

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.AzureAIInference --prerelease

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.Ollama --prerelease

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.Amazon --prerelease

```

Note

Anthropic models are available on the Amazon Bedrock platform. To use Anthropic models, you will need to install the
Amazon connector package.

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.Amazon --prerelease

```

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.Onnx --prerelease

```

For other AI service providers that support the OpenAI chat completion API (e.g., LLM Studio), you can use the OpenAI
chat completion connector.

Bash Copy

```

dotnet add package Microsoft.SemanticKernel.Connectors.OpenAI

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#creating-chat-completion-
services)

## Creating chat completion services

Now that you've installed the necessary packages, you can create chat completion services. Below are the several ways
you can create chat completion services using Semantic Kernel.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#adding-directly-to-the-
kernel)

### Adding directly to the kernel

To add a chat completion service, you can use the following code to add it to the kernel's inner service provider.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-OpenAI)
  * [Mistral](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-Mistral)
  * [Google](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-Google)
  * [Hugging Face](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-HuggingFace)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-AzureAIInference)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-Ollama)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-AmazonBedrock)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-ONNX)
  * [Other](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_3_csharp-other)

C# Copy

```

using Microsoft.SemanticKernel;

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddAzureOpenAIChatCompletion(

  deploymentName: "NAME_OF_YOUR_DEPLOYMENT",

  apiKey: "YOUR_API_KEY",

  endpoint: "YOUR_AZURE_ENDPOINT",

  modelId: "gpt-4", // Optional name of the underlying model if the deployment name doesn't match the model name

  serviceId: "YOUR_SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; if not provided, the HttpClient from the kernel will be used

);

Kernel kernel = kernelBuilder.Build();

```

C# Copy

```

using Microsoft.SemanticKernel;

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddOpenAIChatCompletion(

  modelId: "gpt-4",

  apiKey: "YOUR_API_KEY",

  orgId: "YOUR_ORG_ID", // Optional

  serviceId: "YOUR_SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; if not provided, the HttpClient from the kernel will be used

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Mistral chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddMistralChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  serviceId: "SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Google chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.Connectors.Google;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddGoogleAIGeminiChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  apiVersion: GoogleAIVersion.V1, // Optional

  serviceId: "SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Hugging Face chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddHuggingFaceChatCompletion(

  model: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  serviceId: "SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Azure AI Inference chat completion connector is currently experimental. To use it, you will need to add `#pragma
warning disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddAzureAIInferenceChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  serviceId: "SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Ollama chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddOllamaChatCompletion(

  modelId: "NAME_OF_MODEL",      // E.g. "phi3" if phi3 was downloaded as described above.

  endpoint: new Uri("YOUR_ENDPOINT"), // E.g. "http://localhost:11434" if Ollama has been started in docker as described
above.

  serviceId: "SERVICE_ID"       // Optional; for targeting specific services within Semantic Kernel

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Bedrock chat completion connector which is required for Anthropic is currently experimental. To use it, you will
need to add `#pragma warning disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddBedrockChatCompletionService(

  modelId: "NAME_OF_MODEL",

  bedrockRuntime: amazonBedrockRuntime, // Optional; An instance of IAmazonBedrockRuntime, used to communicate with
Azure Bedrock.

  serviceId: "SERVICE_ID"        // Optional; for targeting specific services within Semantic Kernel

);

Kernel kernel = kernelBuilder.Build();

```

Important

The Bedrock chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddBedrockChatCompletionService(

  modelId: "NAME_OF_MODEL",

  bedrockRuntime: amazonBedrockRuntime, // Optional; An instance of IAmazonBedrockRuntime, used to communicate with
Azure Bedrock.

  serviceId: "SERVICE_ID"        // Optional; for targeting specific services within Semantic Kernel

);

Kernel kernel = kernelBuilder.Build();

```

Important

The ONNX chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0070

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddOnnxRuntimeGenAIChatCompletion(

  modelId: "NAME_OF_MODEL", // E.g. phi-3

  modelPath: "PATH_ON_DISK", // Path to the model on disk e.g. C:\Repos\huggingface\microsoft\Phi-3-mini-4k-instruct-
onnx\cpu_and_mobile\cpu-int4-rtn-block-32

  serviceId: "SERVICE_ID",              // Optional; for targeting specific services within Semantic Kernel

  jsonSerializerOptions: customJsonSerializerOptions // Optional; for providing custom serialization settings for e.g.
function argument / result serialization and parsing.

);

Kernel kernel = kernelBuilder.Build();

```

For other AI service providers that support the OpenAI chat completion API (e.g., LLM Studio), you can use the following
code to reuse the existing OpenAI chat completion connector.

Important

Using custom endpoints with the OpenAI connector is currently experimental. To use it, you will need to add `#pragma
warning disable SKEXP0010`.

C# Copy

```

using Microsoft.SemanticKernel;

#pragma warning disable SKEXP0010

IKernelBuilder kernelBuilder = Kernel.CreateBuilder();

kernelBuilder.AddOpenAIChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Used to point to your service

  serviceId: "SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

Kernel kernel = kernelBuilder.Build();

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#using-dependency-injection)

### Using dependency injection

If you're using dependency injection, you'll likely want to add your AI services directly to the service provider. This
is helpful if you want to create singletons of your AI services and reuse them in transient kernels.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-OpenAI)
  * [Mistral](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-Mistral)
  * [Google](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-Google)
  * [Hugging Face](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-HuggingFace)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-AzureAIInference)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-Ollama)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-AmazonBedrock)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-ONNX)
  * [Other](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_4_csharp-other)

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services.AddAzureOpenAIChatCompletion(

  deploymentName: "NAME_OF_YOUR_DEPLOYMENT",

  apiKey: "YOUR_API_KEY",

  endpoint: "YOUR_AZURE_ENDPOINT",

  modelId: "gpt-4", // Optional name of the underlying model if the deployment name doesn't match the model name

  serviceId: "YOUR_SERVICE_ID" // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services.AddOpenAIChatCompletion(

  modelId: "gpt-4",

  apiKey: "YOUR_API_KEY",

  orgId: "YOUR_ORG_ID", // Optional; for OpenAI deployment

  serviceId: "YOUR_SERVICE_ID" // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Mistral chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddMistralChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  serviceId: "SERVICE_ID" // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Google chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.Connectors.Google;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddGoogleAIGeminiChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  apiVersion: GoogleAIVersion.V1, // Optional

  serviceId: "SERVICE_ID" // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Hugging Face chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddHuggingFaceChatCompletion(

  model: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  serviceId: "SERVICE_ID" // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Azure AI Inference chat completion connector is currently experimental. To use it, you will need to add `#pragma
warning disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddAzureAIInferenceChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  serviceId: "SERVICE_ID" // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Ollama chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddOllamaChatCompletion(

  modelId: "NAME_OF_MODEL",      // E.g. "phi3" if phi3 was downloaded as described above.

  endpoint: new Uri("YOUR_ENDPOINT"), // E.g. "http://localhost:11434" if Ollama has been started in docker as described
above.

  serviceId: "SERVICE_ID"       // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Bedrock chat completion connector which is required for Anthropic is currently experimental. To use it, you will
need to add `#pragma warning disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddBedrockChatCompletionService(

  modelId: "NAME_OF_MODEL",

  bedrockRuntime: amazonBedrockRuntime, // Optional; An instance of IAmazonBedrockRuntime, used to communicate with
Azure Bedrock.

  serviceId: "SERVICE_ID"        // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The Bedrock chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddBedrockChatCompletionService(

  modelId: "NAME_OF_MODEL",

  bedrockRuntime: amazonBedrockRuntime, // Optional; An instance of IAmazonBedrockRuntime, used to communicate with
Azure Bedrock.

  serviceId: "SERVICE_ID"        // Optional; for targeting specific services within Semantic Kernel

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

Important

The ONNX chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0070

builder.Services.AddOnnxRuntimeGenAIChatCompletion(

  modelId: "NAME_OF_MODEL", // E.g. phi-3

  modelPath: "PATH_ON_DISK", // Path to the model on disk e.g. C:\Repos\huggingface\microsoft\Phi-3-mini-4k-instruct-
onnx\cpu_and_mobile\cpu-int4-rtn-block-32

  serviceId: "SERVICE_ID",              // Optional; for targeting specific services within Semantic Kernel

  jsonSerializerOptions: customJsonSerializerOptions // Optional; for providing custom serialization settings for e.g.
function argument / result serialization and parsing.

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

For other AI service providers that support the OpenAI chat completion API (e.g., LLM Studio), you can use the following
code to reuse the existing OpenAI chat completion connector.

Important

Using custom endpoints with the OpenAI connector is currently experimental. To use it, you will need to add `#pragma
warning disable SKEXP0010`.

C# Copy

```

using Microsoft.SemanticKernel;

var builder = Host.CreateApplicationBuilder(args);

#pragma warning disable SKEXP0010

builder.Services.AddOpenAIChatCompletion(

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Used to point to your service

  serviceId: "SERVICE_ID", // Optional; for targeting specific services within Semantic Kernel

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

builder.Services.AddTransient((serviceProvider)=> {

  return new Kernel(serviceProvider);

});

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#creating-standalone-
instances)

### Creating standalone instances

Lastly, you can create instances of the service directly so that you can either add them to a kernel later or use them
directly in your code without ever injecting them into the kernel or in a service provider.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-OpenAI)
  * [Mistral](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-Mistral)
  * [Google](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-Google)
  * [Hugging Face](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-HuggingFace)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-AzureAIInference)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-Ollama)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-AmazonBedrock)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-ONNX)
  * [Other](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_5_csharp-other)

C# Copy

```

using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

AzureOpenAIChatCompletionService chatCompletionService = new (

  deploymentName: "NAME_OF_YOUR_DEPLOYMENT",

  apiKey: "YOUR_API_KEY",

  endpoint: "YOUR_AZURE_ENDPOINT",

  modelId: "gpt-4", // Optional name of the underlying model if the deployment name doesn't match the model name

  httpClient: new HttpClient() // Optional; if not provided, the HttpClient from the kernel will be used

);

```

C# Copy

```

using Microsoft.SemanticKernel.Connectors.OpenAI;

OpenAIChatCompletionService chatCompletionService = new (

  modelId: "gpt-4",

  apiKey: "YOUR_API_KEY",

  organization: "YOUR_ORG_ID", // Optional

  httpClient: new HttpClient() // Optional; if not provided, the HttpClient from the kernel will be used

);

```

Important

The Mistral chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.MistralAI;

#pragma warning disable SKEXP0070

MistralAIChatCompletionService chatCompletionService = new (

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Optional

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

```

Important

The Google chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.Google;

#pragma warning disable SKEXP0070

GoogleAIGeminiChatCompletionService chatCompletionService = new (

  modelId: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  apiVersion: GoogleAIVersion.V1, // Optional

  httpClient: new HttpClient() // Optional; for customizing HTTP client

);

```

Important

The Hugging Face chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.HuggingFace;

#pragma warning disable SKEXP0070

HuggingFaceChatCompletionService chatCompletionService = new (

  model: "NAME_OF_MODEL",

  apiKey: "API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT") // Optional

);

```

Important

The Azure AI Inference chat completion connector is currently experimental. To use it, you will need to add `#pragma
warning disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.AzureAIInference;

#pragma warning disable SKEXP0070

AzureAIInferenceChatCompletionService chatCompletionService = new (

  modelId: "YOUR_MODEL_ID",

  apiKey: "YOUR_API_KEY",

  endpoint: new Uri("YOUR_ENDPOINT"), // Used to point to your service

  httpClient: new HttpClient() // Optional; if not provided, the HttpClient from the kernel will be used

);

```

Important

The Ollama chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.ChatCompletion;

using OllamaSharp;

#pragma warning disable SKEXP0070

using var ollamaClient = new OllamaApiClient(

  uriString: "YOUR_ENDPOINT"  // E.g. "http://localhost:11434" if Ollama has been started in docker as described above.

  defaultModel: "NAME_OF_MODEL" // E.g. "phi3" if phi3 was downloaded as described above.

);

IChatCompletionService chatCompletionService = ollamaClient.AsChatCompletionService();

```

Important

The Bedrock chat completion connector which is required for Anthropic is currently experimental. To use it, you will
need to add `#pragma warning disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.Amazon;

#pragma warning disable SKEXP0070

BedrockChatCompletionService chatCompletionService = new BedrockChatCompletionService(

  modelId: "NAME_OF_MODEL",

  bedrockRuntime: amazonBedrockRuntime // Optional; An instance of IAmazonBedrockRuntime, used to communicate with Azure
Bedrock.

);

```

Important

The Bedrock chat completion connector is currently experimental. To use it, you will need to add `#pragma warning
disable SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.Amazon;

#pragma warning disable SKEXP0070

BedrockChatCompletionService chatCompletionService = new BedrockChatCompletionService(

  modelId: "NAME_OF_MODEL",

  bedrockRuntime: amazonBedrockRuntime // Optional; An instance of IAmazonBedrockRuntime, used to communicate with Azure
Bedrock.

);

```

Important

The ONNX chat completion connector is currently experimental. To use it, you will need to add `#pragma warning disable
SKEXP0070`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.Onnx;

#pragma warning disable SKEXP0070

OnnxRuntimeGenAIChatCompletionService chatCompletionService = new OnnxRuntimeGenAIChatCompletionService(

  modelId: "NAME_OF_MODEL", // E.g. phi-3

  modelPath: "PATH_ON_DISK", // Path to the model on disk e.g. C:\Repos\huggingface\microsoft\Phi-3-mini-4k-instruct-
onnx\cpu_and_mobile\cpu-int4-rtn-block-32

  jsonSerializerOptions: customJsonSerializerOptions // Optional; for providing custom serialization settings for e.g.
function argument / result serialization and parsing.

);

```

For other AI service providers that support the OpenAI chat completion API (e.g., LLM Studio), you can use the following
code to reuse the existing OpenAI chat completion connector.

Important

Using custom endpoints with the OpenAI connector is currently experimental. To use it, you will need to add `#pragma
warning disable SKEXP0010`.

C# Copy

```

using Microsoft.SemanticKernel.Connectors.OpenAI;

#pragma warning disable SKEXP0010

OpenAIChatCompletionService chatCompletionService = new (

  modelId: "gpt-4",

  apiKey: "YOUR_API_KEY",

  organization: "YOUR_ORG_ID", // Optional

  endpoint: new Uri("YOUR_ENDPOINT"), // Used to point to your service

  httpClient: new HttpClient() // Optional; if not provided, the HttpClient from the kernel will be used

);

```

To create a chat completion service, you need to install and import the necessary modules and create an instance of the
service. Below are the steps to install and create a chat completion service for each AI service provider.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#installing-the-necessary-
packages-1)

## Installing the necessary packages

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-OpenAI)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-AzureAIInference)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-AmazonBedrock)
  * [Google AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-Google)
  * [Vertex AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-VertexAI)
  * [Mistral AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-MistralAI)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-Ollama)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_6_python-ONNX)

The Semantic Kernel package comes with all the necessary packages to use Azure OpenAI. There are no additional packages
required to use Azure OpenAI.

The Semantic Kernel package comes with all the necessary packages to use OpenAI. There are no additional packages
required to use OpenAI.

Bash Copy

```

pip install semantic-kernel[azure]

```

Bash Copy

```

pip install semantic-kernel[anthropic]

```

Bash Copy

```

pip install semantic-kernel[aws]

```

Bash Copy

```

pip install semantic-kernel[google]

```

Bash Copy

```

pip install semantic-kernel[google]

```

Bash Copy

```

pip install semantic-kernel[mistralai]

```

Bash Copy

```

pip install semantic-kernel[ollama]

```

Bash Copy

```

pip install semantic-kernel[onnx]

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#creating-a-chat-completion-
service)

## Creating a chat completion service

Tip

There are three methods to supply the required information to AI services. You may either provide the information
directly through the constructor, set the necessary environment variables, or create a .env file within your project
directory containing the environment variables. You can visit this page to find all the required environment variables
for each AI service provider:

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-OpenAI)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-AzureAIInference)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-AmazonBedrock)
  * [Google AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-Google)
  * [Vertex AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-VertexAI)
  * [Mistral AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-MistralAI)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-Ollama)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_7_python-ONNX)

Python Copy

```

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

chat_completion_service = AzureChatCompletion(

  deployment_name="my-deployment",

  api_key="my-api-key",

  endpoint="my-api-endpoint", # Used to point to your service

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

# You can do the following if you have set the necessary environment variables or created a .env file

chat_completion_service = AzureChatCompletion(service_id="my-service-id")

```

Note

The `AzureChatCompletion` service also supports [Microsoft Entra](https://learn.microsoft.com/en-
us/entra/identity/authentication/overview-authentication) authentication. If you don't provide an API key, the service
will attempt to authenticate using the Entra token.

Python Copy

```

from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

chat_completion_service = OpenAIChatCompletion(

  ai_model_id="my-deployment",

  api_key="my-api-key",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

# You can do the following if you have set the necessary environment variables or created a .env file

chat_completion_service = OpenAIChatCompletion(service_id="my-service-id")

```

Python Copy

```

from semantic_kernel.connectors.ai.azure_ai_inference import AzureAIInferenceChatCompletion

chat_completion_service = AzureAIInferenceChatCompletion(

  ai_model_id="my-deployment",

  api_key="my-api-key",

  endpoint="my-api-endpoint", # Used to point to your service

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

# You can do the following if you have set the necessary environment variables or created a .env file

chat_completion_service = AzureAIInferenceChatCompletion(ai_model_id="my-deployment", service_id="my-service-id")

# You can also use an Azure OpenAI deployment with the Azure AI Inference service

from azure.ai.inference.aio import ChatCompletionsClient

from azure.identity.aio import DefaultAzureCredential

chat_completion_service = AzureAIInferenceChatCompletion(

  ai_model_id="my-deployment",

  client=ChatCompletionsClient(

    endpoint=f"{str(endpoint).strip('/')}/openai/deployments/{deployment_name}",
    credential=DefaultAzureCredential(),
    credential_scopes=["https://cognitiveservices.azure.com/.default"],
  ),

)

```

Note

The `AzureAIInferenceChatCompletion` service also supports [Microsoft Entra](https://learn.microsoft.com/en-
us/entra/identity/authentication/overview-authentication) authentication. If you don't provide an API key, the service
will attempt to authenticate using the Entra token.

Python Copy

```

from semantic_kernel.connectors.ai.anthropic import AnthropicChatCompletion

chat_completion_service = AnthropicChatCompletion(

  chat_model_id="model-id",

  api_key="my-api-key",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

Python Copy

```

from semantic_kernel.connectors.ai.bedrock import BedrockChatCompletion

chat_completion_service = BedrockChatCompletion(

  model_id="model-id",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

Note

Amazon Bedrock does not accept an API key. Follow this to configure your environment.

Python Copy

```

from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatCompletion

chat_completion_service = GoogleAIChatCompletion(

  gemini_model_id="model-id",

  api_key="my-api-key",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

Tip

Users can access Google's Gemini models via Google AI Studio or Google Vertex platform. Follow this to configure your
environment.

Python Copy

```

from semantic_kernel.connectors.ai.google.vertex_ai import VertexAIChatCompletion

chat_completion_service = VertexAIChatCompletion(

  project_id="my-project-id",

  gemini_model_id="model-id",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

Tip

Users can access Google's Gemini models via Google AI Studio or Google Vertex platform. Follow this to configure your
environment.

Python Copy

```

from semantic_kernel.connectors.ai.mistral_ai import MistralAIChatCompletion

chat_completion_service = MistralAIChatCompletion(

  ai_model_id="model-id",

  api_key="my-api-key",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

Python Copy

```

from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

chat_completion_service = OllamaChatCompletion(

  ai_model_id="model-id",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

Tip

Learn more about Ollama and download the necessary software from .

Python Copy

```

from semantic_kernel.connectors.ai.onnx import OnnxGenAIChatCompletion

chat_completion_service = OnnxGenAIChatCompletion(

  template="phi3v",

  ai_model_path="model-path",

  service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel

)

```

You can start using the completion service right away or add the chat completion service to a kernel. You can use the
following code to add a service to the kernel.

Python Copy

```

from semantic_kernel import Kernel

# Initialize the kernel

kernel = Kernel()

# Add the chat completion service created above to the kernel

kernel.add_service(chat_completion_service)

```

You can create instances of the chat completion service directly and either add them to a kernel or use them directly in
your code without injecting them into the kernel. The following code shows how to create a a chat completion service and
add it to the kernel.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_8_java-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_8_java-OpenAI)

Java Copy

```

import com.azure.ai.openai.OpenAIAsyncClient;

import com.azure.ai.openai.OpenAIClientBuilder;

import com.microsoft.semantickernel.Kernel;

import com.microsoft.semantickernel.services.chatcompletion.ChatCompletionService;

// Create the client

OpenAIAsyncClient client = new OpenAIClientBuilder()

  .credential(azureOpenAIClientCredentials)

  .endpoint(azureOpenAIClientEndpoint)

  .buildAsyncClient();

// Create the chat completion service

ChatCompletionService openAIChatCompletion = OpenAIChatCompletion.builder()

  .withOpenAIAsyncClient(client)

  .withModelId(modelId)

  .build();

// Initialize the kernel

Kernel kernel = Kernel.builder()

  .withAIService(ChatCompletionService.class, openAIChatCompletion)

  .build();

```

Java Copy

```

import com.azure.ai.openai.OpenAIAsyncClient;

import com.azure.ai.openai.OpenAIClientBuilder;

import com.microsoft.semantickernel.Kernel;

import com.microsoft.semantickernel.services.chatcompletion.ChatCompletionService;

// Create the client

OpenAIAsyncClient client = new OpenAIClientBuilder()

  .credential(openAIClientCredentials)

  .buildAsyncClient();

// Create the chat completion service

ChatCompletionService openAIChatCompletion = OpenAIChatCompletion.builder()

  .withOpenAIAsyncClient(client)

  .withModelId(modelId)

  .build();

// Initialize the kernel

Kernel kernel = Kernel.builder()

  .withAIService(ChatCompletionService.class, openAIChatCompletion)

  .build();

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#retrieving-chat-completion-
services)

## Retrieving chat completion services

Once you've added chat completion services to your kernel, you can retrieve them using the get service method. Below is
an example of how you can retrieve a chat completion service from the kernel.

C# Copy

```

var chatCompletionService = kernel.GetRequiredService<IChatCompletionService>();

```

Python Copy

```

from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase

# Retrieve the chat completion service by type

chat_completion_service = kernel.get_service(type=ChatCompletionClientBase)

# Retrieve the chat completion service by id

chat_completion_service = kernel.get_service(service_id="my-service-id")

# Retrieve the default inference settings

execution_settings = kernel.get_prompt_execution_settings_from_service_id("my-service-id")

```

Java Copy

```

ChatCompletionService chatCompletionService = kernel.getService(ChatCompletionService.class);

```

Tip

Adding the chat completion service to the kernel is not required if you don't need to use other services in the kernel.
You can use the chat completion service directly in your code.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#using-chat-completion-
services)

## Using chat completion services

Now that you have a chat completion service, you can use it to generate responses from an AI agent. There are two main
ways to use a chat completion service:

  * **Non-streaming** : You wait for the service to generate an entire response before returning it to the user.
  * **Streaming** : Individual chunks of the response are generated and returned to the user as they are created.

Before getting started, you will need to manually create an execution settings instance to use the chat completion
service if you did not register the service with the kernel.

  * [Azure OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-AzureOpenAI)
  * [OpenAI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-OpenAI)
  * [Azure AI Inference](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-AzureAIInference)
  * [Anthropic](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-Anthropic)
  * [Amazon Bedrock](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-AmazonBedrock)
  * [Google AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-Google)
  * [Vertex AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-VertexAI)
  * [Mistral AI](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-MistralAI)
  * [Ollama](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-Ollama)
  * [ONNX](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#tabpanel_9_python-ONNX)

Python Copy

```

from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings

execution_settings = OpenAIChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings

execution_settings = OpenAIChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.azure_ai_inference import AzureAIInferenceChatPromptExecutionSettings

execution_settings = AzureAIInferenceChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.anthropic import AnthropicChatPromptExecutionSettings

execution_settings = AnthropicChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.bedrock import BedrockChatPromptExecutionSettings

execution_settings = BedrockChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatPromptExecutionSettings

execution_settings = GoogleAIChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.google.vertex_ai import VertexAIChatPromptExecutionSettings

execution_settings = VertexAIChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.mistral_ai import MistralAIChatPromptExecutionSettings

execution_settings = MistralAIChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.ollama import OllamaChatPromptExecutionSettings

execution_settings = OllamaChatPromptExecutionSettings()

```

Python Copy

```

from semantic_kernel.connectors.ai.onnx import OnnxGenAIPromptExecutionSettings

execution_settings = OnnxGenAIPromptExecutionSettings()

```

Tip

To see what you can configure in the execution settings, you can check the class definition in the or check out the [API
documentation](https://learn.microsoft.com/en-us/python/api/semantic-kernel/semantic_kernel.connectors.ai).

Below are the two ways you can use a chat completion service to generate responses.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#non-streaming-chat-
completion)

### Non-streaming chat completion

To use non-streaming chat completion, you can use the following code to generate a response from the AI agent.

C# Copy

```

ChatHistory history = [];

history.AddUserMessage("Hello, how are you?");

var response = await chatCompletionService.GetChatMessageContentAsync(

  history,

  kernel: kernel

);

```

Python Copy

```

chat_history = ChatHistory()

chat_history.add_user_message("Hello, how are you?")

response = await chat_completion.get_chat_message_content(

  chat_history=history,

  settings=execution_settings,

)

```

Java Copy

```

ChatHistory history = new ChatHistory();

history.addUserMessage("Hello, how are you?");

InvocationContext optionalInvocationContext = null;

List<ChatMessageContent<?>> response = chatCompletionService.getChatMessageContentsAsync(

  history,

  kernel,

  optionalInvocationContext

);

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#streaming-chat-completion)

### Streaming chat completion

To use streaming chat completion, you can use the following code to generate a response from the AI agent.

C# Copy

```

ChatHistory history = [];

history.AddUserMessage("Hello, how are you?");

var response = chatCompletionService.GetStreamingChatMessageContentsAsync(

  chatHistory: history,

  kernel: kernel

);

await foreach (var chunk in response)

{

  Console.Write(chunk);

}

```

Python Copy

```

chat_history = ChatHistory()

chat_history.add_user_message("Hello, how are you?")

response = chat_completion.get_streaming_chat_message_content(

  chat_history=history,

  settings=execution_settings,

)

async for chunk in response:

  print(chunk, end="")

```

Note

Semantic Kernel for Java does not support the streaming response model.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#next-steps)

## Next steps

Now that you've added chat completion services to your Semantic Kernel project, you can start creating conversations
with your AI agent. To learn more about using a chat completion service, check out the following articles:

[Using the chat history object](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-
completion/chat-history)

[Optimizing function calling with chat completion](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-
services/chat-completion/function-calling)

## Additional resources

Documentation

  * [ Creating and managing a chat history object ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/chat-history?source=recommendations)
Use chat history to maintain a record of messages in a chat session

  * [ Semantic Kernel Components ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/semantic-kernel-components?source=recommendations)
Describes the relationship between the different semantic kernel components

  * [ Multi-modal chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/multi-modal-chat-completion?source=recommendations)
Doing chat completion with images

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

  * [ Understanding the kernel in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel?source=recommendations)
Learn about the central component of Semantic Kernel and how it works

  * [ Add AI services to Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/?source=recommendations)
Learn how to bring multiple AI services to your Semantic Kernel project.

  * [ AI Integrations for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/integrations?source=recommendations)
Learn which features are available for C#, Python, and Java through integrations.

  * [ Supported languages for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages?source=recommendations)
Learn which features are available for C#, Python, and Java.

Show 5 more

Training

Module

[ Generate text and conversations with .NET and Azure OpenAI Completions - Training ](https://learn.microsoft.com/en-
us/training/modules/open-ai-dotnet-text-completions/?source=recommendations)

Learn how to use the .NET SDK with the Azure OpenAI service to have your applications carry on conversations with users
in natural language.

Certification

[ Microsoft Certified: Azure AI Fundamentals - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-fundamentals/?source=recommendations)

Demonstrate fundamental AI concepts related to the development of software and services of Microsoft Azure to create AI
solutions.

## Additional resources

Training

Module

[ Generate text and conversations with .NET and Azure OpenAI Completions - Training ](https://learn.microsoft.com/en-
us/training/modules/open-ai-dotnet-text-completions/?source=recommendations)

Learn how to use the .NET SDK with the Azure OpenAI service to have your applications carry on conversations with users
in natural language.

Certification

[ Microsoft Certified: Azure AI Fundamentals - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-fundamentals/?source=recommendations)

Demonstrate fundamental AI concepts related to the development of software and services of Microsoft Azure to create AI
solutions.

Documentation

  * [ Creating and managing a chat history object ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/chat-history?source=recommendations)
Use chat history to maintain a record of messages in a chat session

  * [ Semantic Kernel Components ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/semantic-kernel-components?source=recommendations)
Describes the relationship between the different semantic kernel components

  * [ Multi-modal chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/multi-modal-chat-completion?source=recommendations)
Doing chat completion with images

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

  * [ Understanding the kernel in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel?source=recommendations)
Learn about the central component of Semantic Kernel and how it works

  * [ Add AI services to Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/?source=recommendations)
Learn how to bring multiple AI services to your Semantic Kernel project.

  * [ AI Integrations for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/integrations?source=recommendations)
Learn which features are available for C#, Python, and Java through integrations.

  * [ Supported languages for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages?source=recommendations)
Learn which features are available for C#, Python, and Java.

Show 5 more

### In this article

