Table of contents[ Read in English ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/ "Read in
English") Add to Collections Add to plan

#### Share via

Print

Table of contents

# Adding AI services to Semantic Kernel

  * Article
  * 03/06/2025
  * 5 contributors

Feedback

## In this article

One of the main features of Semantic Kernel is its ability to add different AI services to the kernel. This allows you
to easily swap out different AI services to compare their performance and to leverage the best model for your needs. In
this section, we will provide sample code for adding different AI services to the kernel.

Within Semantic Kernel, there are interfaces for the most popular AI tasks. In the table below, you can see the services
that are supported by each of the SDKs.

Expand table

Services | C# | Python | Java | Notes  
---|---|---|---|---  
[Chat completion](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/) | ✅ | ✅ | ✅  
Text generation | ✅ | ✅ | ✅  
Embedding generation (Experimental) | ✅ | ✅ | ✅  
Text-to-image (Experimental) | ✅ | ✅ | ❌  
Image-to-text (Experimental) | ✅ | ❌ | ❌  
Text-to-audio (Experimental) | ✅ | ✅ | ❌  
Audio-to-text (Experimental) | ✅ | ✅ | ❌  
[Realtime](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/realtime) (Experimental) | ❌ | ✅ | ❌  
Tip

In most scenarios, you will only need to add chat completion to your kernel, but to support multi-modal AI, you can add
any of the above services to your kernel.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/#next-steps)

## Next steps

To learn more about each of the services, please refer to the specific articles for each service type. In each of the
articles we provide sample code for adding the service to the kernel across multiple AI service providers.

[Learn about chat completion](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/)

## Additional resources

Documentation

  * [ Semantic Kernel Components ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/semantic-kernel-components?source=recommendations)
Describes the relationship between the different semantic kernel components

  * [ Creating and managing a chat history object ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/chat-history?source=recommendations)
Use chat history to maintain a record of messages in a chat session

  * [ Understanding the kernel in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel?source=recommendations)
Learn about the central component of Semantic Kernel and how it works

  * [ Multi-modal chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/multi-modal-chat-completion?source=recommendations)
Doing chat completion with images

  * [ Add chat completion services to Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/?source=recommendations)
Learn how to add gpt-4, Mistral, Google, and other chat completion services to your Semantic Kernel project.

  * [ AI Integrations for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/integrations?source=recommendations)
Learn which features are available for C#, Python, and Java through integrations.

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

  * [ In-depth Semantic Kernel Demos ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/detailed-samples?source=recommendations)
Go deeper with additional Demos to learn how to use Semantic Kernel.

Show 5 more

Training

Learning path

[ Develop generative AI apps with Azure OpenAI and Semantic Kernel - Training ](https://learn.microsoft.com/en-
us/training/paths/develop-ai-agents-azure-open-ai-semantic-kernel-sdk/?source=recommendations)

Develop generative AI apps with Azure OpenAI and Semantic Kernel

Certification

[ Microsoft Certified: Azure AI Engineer Associate - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-engineer/?source=recommendations)

Design and implement an Azure AI solution using Azure AI services, Azure AI Search, and Azure Open AI.

## Additional resources

Training

Learning path

[ Develop generative AI apps with Azure OpenAI and Semantic Kernel - Training ](https://learn.microsoft.com/en-
us/training/paths/develop-ai-agents-azure-open-ai-semantic-kernel-sdk/?source=recommendations)

Develop generative AI apps with Azure OpenAI and Semantic Kernel

Certification

[ Microsoft Certified: Azure AI Engineer Associate - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-engineer/?source=recommendations)

Design and implement an Azure AI solution using Azure AI services, Azure AI Search, and Azure Open AI.

Documentation

  * [ Semantic Kernel Components ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/semantic-kernel-components?source=recommendations)
Describes the relationship between the different semantic kernel components

  * [ Creating and managing a chat history object ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/chat-history?source=recommendations)
Use chat history to maintain a record of messages in a chat session

  * [ Understanding the kernel in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel?source=recommendations)
Learn about the central component of Semantic Kernel and how it works

  * [ Multi-modal chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/multi-modal-chat-completion?source=recommendations)
Doing chat completion with images

  * [ Add chat completion services to Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/?source=recommendations)
Learn how to add gpt-4, Mistral, Google, and other chat completion services to your Semantic Kernel project.

  * [ AI Integrations for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/integrations?source=recommendations)
Learn which features are available for C#, Python, and Java through integrations.

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

  * [ In-depth Semantic Kernel Demos ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/detailed-samples?source=recommendations)
Go deeper with additional Demos to learn how to use Semantic Kernel.

Show 5 more

### In this article

