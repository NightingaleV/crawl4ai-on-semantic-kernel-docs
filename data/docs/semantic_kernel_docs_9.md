
# Getting started with Semantic Kernel

  * Article
  * 11/08/2024
  * 11 contributors

Feedback

## In this article

  1. [Installing the SDK](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#installing-the-sdk)
  2. [Quickly get started with notebooks](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#quickly-get-started-with-notebooks)
  3. [Writing your first console app](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#writing-your-first-console-app)
  4. [Understanding the code](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#understanding-the-code)
  5. [Next steps](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#next-steps)

In just a few steps, you can build your first AI agent with Semantic Kernel in either Python, .NET, or Java. This guide
will show you how to...

  * Install the necessary packages
  * Create a back-and-forth conversation with an AI
  * Give an AI agent the ability to run your code
  * Watch the AI create plans on the fly

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#installing-the-sdk)

## Installing the SDK

Semantic Kernel has several NuGet packages available. For most scenarios, however, you typically only need
`Microsoft.SemanticKernel`.

You can install it using the following command:

Bash Copy

```

dotnet add package Microsoft.SemanticKernel

```

For the full list of Nuget packages, please refer to the [supported languages article](https://learn.microsoft.com/en-
us/semantic-kernel/get-started/supported-languages).

Instructions for accessing the `SemanticKernel` Python package is available . It's as easy as:

PyPI Copy

```

pip install semantic-kernel

```

Instructions for accessing the `SemanticKernel` Java package is available . It's as easy as:

XML Copy

```

<dependencyManagement>

  <dependencies>

    <dependency>
      <groupId>com.microsoft.semantic-kernel</groupId>
      <artifactId>semantickernel-bom</artifactId>
      <version>${sk.version}</version>
      <type>pom</type>
      <scope>import</scope>
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

  <artifactId>semantickernel-aiservices-openai</artifactId>

</dependency>

</dependencies>

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#quickly-get-started-with-notebooks)

## Quickly get started with notebooks

If you're a Python or C# developer, you can quickly get started with our notebooks. These notebooks provide step-by-step
guides on how to use Semantic Kernel to build AI agents.

![Semantic Kernel notebooks](https://learn.microsoft.com/en-us/semantic-
kernel/media/python_getting_started_notebooks.png)

To get started, follow these steps:

  1. Clone the 
  2. Open the repo in Visual Studio Code
  3. Navigate to 
  4. Open _00-getting-started.ipynb_ to get started setting your environment and creating your first AI agent!

To get started, follow these steps:

  1. Clone the 
  2. Open the repo in Visual Studio Code
  3. Navigate to 
  4. Open _00-getting-started.ipynb_ to get started setting your environment and creating your first AI agent!

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#writing-your-first-console-app)

## Writing your first console app

  1. Create a new .NET Console project using this command:

Bash Copy

```

dotnet new console

```

  1. Install the following .NET dependencies:

Bash Copy

```

dotnet add package Microsoft.SemanticKernel

dotnet add package Microsoft.Extensions.Logging

dotnet add package Microsoft.Extensions.Logging.Console

```

  1. Replace the content of the `Program.cs` file with this code:

C# Copy

```

// Import packages

using Microsoft.Extensions.DependencyInjection;

using Microsoft.Extensions.Logging;

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.ChatCompletion;

using Microsoft.SemanticKernel.Connectors.OpenAI;

// Populate values from your OpenAI deployment

var modelId = "";

var endpoint = "";

var apiKey = "";

// Create a kernel with Azure OpenAI chat completion

var builder = Kernel.CreateBuilder().AddAzureOpenAIChatCompletion(modelId, endpoint, apiKey);

// Add enterprise components

builder.Services.AddLogging(services => services.AddConsole().SetMinimumLevel(LogLevel.Trace));

// Build the kernel

Kernel kernel = builder.Build();

var chatCompletionService = kernel.GetRequiredService<IChatCompletionService>();

// Add a plugin (the LightsPlugin class is defined below)

kernel.Plugins.AddFromType<LightsPlugin>("Lights");

// Enable planning

OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new() 

{

  FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()

};

// Create a history store the conversation

var history = new ChatHistory();

// Initiate a back-and-forth chat

string? userInput;

do {

  // Collect user input

  Console.Write("User > ");

  userInput = Console.ReadLine();

  // Add user input

  history.AddUserMessage(userInput);

  // Get the response from the AI

  var result = await chatCompletionService.GetChatMessageContentAsync(

    history,
    executionSettings: openAIPromptExecutionSettings,
    kernel: kernel);
  // Print the results

  Console.WriteLine("Assistant > " + result);

  // Add the message from the agent to the chat history

  history.AddMessage(result.Role, result.Content ?? string.Empty);

} while (userInput is not null);

```

Python Copy

```

import asyncio

from semantic_kernel import Kernel

from semantic_kernel.utils.logging import setup_logging

from semantic_kernel.functions import kernel_function

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior

from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase

from semantic_kernel.contents.chat_history import ChatHistory

from semantic_kernel.functions.kernel_arguments import KernelArguments

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (

  AzureChatPromptExecutionSettings,

)

async def main():

  # Initialize the kernel

  kernel = Kernel()

  # Add Azure OpenAI chat completion

  chat_completion = AzureChatCompletion(

    deployment_name="your_models_deployment_name",
    api_key="your_api_key",
    base_url="your_base_url",
  )

  kernel.add_service(chat_completion)

  # Set the logging level for semantic_kernel.kernel to DEBUG.

  setup_logging()

  logging.getLogger("kernel").setLevel(logging.DEBUG)

  # Add a plugin (the LightsPlugin class is defined below)

  kernel.add_plugin(

    LightsPlugin(),
    plugin_name="Lights",
  )

  # Enable planning

  execution_settings = AzureChatPromptExecutionSettings()

  execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

  # Create a history of the conversation

  history = ChatHistory()

  # Initiate a back-and-forth chat

  userInput = None

  while True:

    # Collect user input
    userInput = input("User > ")
    # Terminate the loop if the user says "exit"
    if userInput == "exit":
      break
    # Add user input to the history
    history.add_user_message(userInput)
    # Get the response from the AI
    result = await chat_completion.get_chat_message_content(
      chat_history=history,
      settings=execution_settings,
      kernel=kernel,
    )
    # Print the results
    print("Assistant > " + str(result))
    # Add the message from the agent to the chat history
    history.add_message(result)
# Run the main function

if __name__ == "__main__":

  asyncio.run(main())

```

Java Copy

```

OpenAIAsyncClient client = new OpenAIClientBuilder()

  .credential(new AzureKeyCredential(AZURE_CLIENT_KEY))

  .endpoint(CLIENT_ENDPOINT)

  .buildAsyncClient();

// Import the LightsPlugin

KernelPlugin lightPlugin = KernelPluginFactory.createFromObject(new LightsPlugin(),

  "LightsPlugin");

// Create your AI service client

ChatCompletionService chatCompletionService = OpenAIChatCompletion.builder()

  .withModelId(MODEL_ID)

  .withOpenAIAsyncClient(client)

  .build();

// Create a kernel with Azure OpenAI chat completion and plugin

Kernel kernel = Kernel.builder()

  .withAIService(ChatCompletionService.class, chatCompletionService)

  .withPlugin(lightPlugin)

  .build();

// Add a converter to the kernel to show it how to serialise LightModel objects into a prompt

ContextVariableTypes

  .addGlobalConverter(

    ContextVariableTypeConverter.builder(LightModel.class)
      .toPromptString(new Gson()::toJson)
      .build());
// Enable planning

InvocationContext invocationContext = new InvocationContext.Builder()

  .withReturnMode(InvocationReturnMode.LAST_MESSAGE_ONLY)

  .withToolCallBehavior(ToolCallBehavior.allowAllKernelFunctions(true))

  .build();

// Create a history to store the conversation

ChatHistory history = new ChatHistory();

// Initiate a back-and-forth chat

Scanner scanner = new Scanner(System.in);

String userInput;

do {

 // Collect user input

 System.out.print("User > ");

 userInput = scanner.nextLine();

 // Add user input

 history.addUserMessage(userInput);

 // Prompt AI for response to users input

 List<ChatMessageContent<?>> results = chatCompletionService

   .getChatMessageContentsAsync(history, kernel, invocationContext)

   .block();

 for (ChatMessageContent<?> result : results) {

  // Print the results

  if (result.getAuthorRole() == AuthorRole.ASSISTANT && result.getContent() != null) {

   System.out.println("Assistant > " + result);

  }

  // Add the message from the agent to the chat history

  history.addMessage(result);

 }

} while (userInput != null && !userInput.isEmpty());

```

The following back-and-forth chat should be similar to what you see in the console. The function calls have been added
below to demonstrate how the AI leverages the plugin behind the scenes.

Expand table

Role | Message  
---|---  
🔵 **User** | Please toggle the light  
🔴 **Assistant (function call)** | `LightsPlugin.GetState()`  
🟢 **Tool** | `off`  
🔴 **Assistant (function call)** | `LightsPlugin.ChangeState(true)`  
🟢 **Tool** | `on`  
🔴 **Assistant** | The light is now on  
If you're interested in understanding more about the code above, we'll break it down in the next section.

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#understanding-the-code)

## Understanding the code

To make it easier to get started building enterprise apps with Semantic Kernel, we've created a step-by-step that guides
you through the process of creating a kernel and using it to interact with AI services.

![Semantic Kernel Python map](https://learn.microsoft.com/en-us/semantic-kernel/media/updatedpythonmap.png)

![Semantic Kernel DotNET map](https://learn.microsoft.com/en-us/semantic-kernel/media/dotnetmap.png)

In the following sections, we'll unpack the above sample by walking through steps **1** , **2** , **3** , **4** , **6**
, **9** , and **10**. Everything you need to build a simple agent that is powered by an AI service and can run your
code.

  * [Import packages](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#1-import-packages)
  * [Add AI services](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#2-add-ai-services)
  * [Enterprise components](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#3-add-enterprise-services)
  * [Build the kernel](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#4-build-the-kernel-and-retrieve-services)
  * Add memory (skipped)
  * [Add plugins](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#6-add-plugins)
  * Create kernel arguments (skipped)
  * Create prompts (skipped)
  * [Planning](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#9-planning)
  * [Invoke](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#10-invoke)

  * [Import packages](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#1-import-packages)
  * [Add AI services](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#2-add-ai-services)
  * [Build the kernel](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#4-build-the-kernel-and-retrieve-services)
  * Add memory (skipped)
  * [Add plugins](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#6-add-plugins)
  * Create kernel arguments (skipped)
  * Create prompts (skipped)
  * [Planning](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#9-planning)
  * [Invoke](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#10-invoke)

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#1-import-packages)

### 1) Import packages

For this sample, we first started by importing the following packages:

C# Copy

```

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.ChatCompletion;

using Microsoft.SemanticKernel.Connectors.OpenAI;

```

Python Copy

```

import asyncio

from semantic_kernel import Kernel

from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior

from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase

from semantic_kernel.contents.chat_history import ChatHistory

from semantic_kernel.functions.kernel_arguments import KernelArguments

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (

  AzureChatPromptExecutionSettings,

)

```

Java Copy

```

import com.microsoft.semantickernel.Kernel;

import com.microsoft.semantickernel.aiservices.openai.chatcompletion.OpenAIChatCompletion;

import com.microsoft.semantickernel.contextvariables.ContextVariableTypeConverter;

import com.microsoft.semantickernel.contextvariables.ContextVariableTypes;

import com.microsoft.semantickernel.orchestration.InvocationContext;

import com.microsoft.semantickernel.orchestration.InvocationReturnMode;

import com.microsoft.semantickernel.orchestration.ToolCallBehavior;

import com.microsoft.semantickernel.plugin.KernelPlugin;

import com.microsoft.semantickernel.plugin.KernelPluginFactory;

import com.microsoft.semantickernel.services.chatcompletion.AuthorRole;

import com.microsoft.semantickernel.services.chatcompletion.ChatCompletionService;

import com.microsoft.semantickernel.services.chatcompletion.ChatHistory;

import com.microsoft.semantickernel.services.chatcompletion.ChatMessageContent;

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#2-add-ai-services)

### 2) Add AI services

Afterwards, we add the most important part of a kernel: the AI services that you want to use. In this example, we added
an Azure OpenAI chat completion service to the kernel builder.

Note

In this example, we used Azure OpenAI, but you can use any other chat completion service. To see the full list of
supported services, refer to the [supported languages article](https://learn.microsoft.com/en-us/semantic-kernel/get-
started/supported-languages). If you need help creating a different service, refer to the [AI services
article](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/). There, you'll find guidance on how to
use OpenAI or Azure OpenAI models as services.

C# Copy

```

// Create kernel

var builder = Kernel.CreateBuilder()

builder.AddAzureOpenAIChatCompletion(modelId, endpoint, apiKey);

```

Python Copy

```

# Initialize the kernel

kernel = Kernel()

# Add Azure OpenAI chat completion

kernel.add_service(AzureChatCompletion(

  deployment_name="your_models_deployment_name",

  api_key="your_api_key",

  base_url="your_base_url",

))

```

Java Copy

```

// Create your AI service client

ChatCompletionService chatCompletionService = OpenAIChatCompletion.builder()

  .withModelId(MODEL_ID)

  .withOpenAIAsyncClient(client)

  .build();

// Create a kernel with Azure OpenAI chat completion and plugin

Kernel kernel = Kernel.builder()

  .withAIService(ChatCompletionService.class, chatCompletionService)

  .withPlugin(lightPlugin)

  .build();

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#3-add-enterprise-services)

### 3) Add enterprise services

One of the main benefits of using Semantic Kernel is that it supports enterprise-grade services. In this sample, we
added the logging service to the kernel to help debug the AI agent.

C# Copy

```

builder.Services.AddLogging(services => services.AddConsole().SetMinimumLevel(LogLevel.Trace));

```

Python Copy

```

import logging

# Set the logging level for semantic_kernel.kernel to DEBUG.

logging.basicConfig(

  format="[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s",

  datefmt="%Y-%m-%d %H:%M:%S",

)

logging.getLogger("kernel").setLevel(logging.DEBUG)

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#4-build-the-kernel-and-retrieve-
services)

### 4) Build the kernel and retrieve services

Once the services have been added, we then build the kernel and retrieve the chat completion service for later use.

C# Copy

```

Kernel kernel = builder.Build();

// Retrieve the chat completion service

var chatCompletionService = kernel.Services.GetRequiredService<IChatCompletionService>();

```

Once the kernel has been configured, we then retrieve the chat completion service for later use.

Note

In Python, you don't need to explicitly build the kernel. Instead, you can access the services directly from the kernel
object.

Python Copy

```

chat_completion : AzureChatCompletion = kernel.get_service(type=ChatCompletionClientBase)

```

Java Copy

```

// Create a kernel with Azure OpenAI chat completion and plugin

Kernel kernel = Kernel.builder()

  .withAIService(ChatCompletionService.class, chatCompletionService)

  .withPlugin(lightPlugin)

  .build();

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#6-add-plugins)

### 6) Add plugins

With plugins, can give your AI agent the ability to run your code to retrieve information from external sources or to
perform actions. In the above example, we added a plugin that allows the AI agent to interact with a light bulb. Below,
we'll show you how to create this plugin.

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#create-a-native-plugin)

#### Create a native plugin

Below, you can see that creating a native plugin is as simple as creating a new class.

In this example, we've created a plugin that can manipulate a light bulb. While this is a simple example, this plugin
quickly demonstrates how you can support both...

  1. [Retrieval Augmented Generation (RAG)](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag) by providing the AI agent with the state of the light bulb
  2. And [task automation](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions) by allowing the AI agent to turn the light bulb on or off.

In your own code, you can create a plugin that interacts with any external service or API to achieve similar results.

C# Copy

```

using System.ComponentModel;

using System.Text.Json.Serialization;

using Microsoft.SemanticKernel;

public class LightsPlugin

{

  // Mock data for the lights

  private readonly List<LightModel> lights = new()

  {

   new LightModel { Id = 1, Name = "Table Lamp", IsOn = false },

   new LightModel { Id = 2, Name = "Porch light", IsOn = false },

   new LightModel { Id = 3, Name = "Chandelier", IsOn = true }

  };

  [KernelFunction("get_lights")]

  [Description("Gets a list of lights and their current state")]

  public async Task<List<LightModel>> GetLightsAsync()

  {

   return lights;

  }

  [KernelFunction("change_state")]

  [Description("Changes the state of the light")]

  public async Task<LightModel?> ChangeStateAsync(int id, bool isOn)

  {

   var light = lights.FirstOrDefault(light => light.Id == id);

   if (light == null)

   {

     return null;
   }

   // Update the light with the new state

   light.IsOn = isOn;

   return light;

  }

}

public class LightModel

{

  [JsonPropertyName("id")]

  public int Id { get; set; }

  [JsonPropertyName("name")]

  public string Name { get; set; }

  [JsonPropertyName("is_on")]

  public bool? IsOn { get; set; }

}

```

Python Copy

```

from typing import Annotated

from semantic_kernel.functions import kernel_function

class LightsPlugin:

  lights = [

    {"id": 1, "name": "Table Lamp", "is_on": False},
    {"id": 2, "name": "Porch light", "is_on": False},
    {"id": 3, "name": "Chandelier", "is_on": True},
  ]

  @kernel_function(

    name="get_lights",
    description="Gets a list of lights and their current state",
  )

  def get_state(

    self,
  ) -> str:

    """Gets a list of lights and their current state."""
    return self.lights
  @kernel_function(

    name="change_state",
    description="Changes the state of the light",
  )

  def change_state(

    self,
    id: int,
    is_on: bool,
  ) -> str:

    """Changes the state of the light."""
    for light in self.lights:
      if light["id"] == id:
        light["is_on"] = is_on
        return light
    return None

```

Java Copy

```

public class LightsPlugin {

 // Mock data for the lights

 private final Map<Integer, LightModel> lights = new HashMap<>();

 public LightsPlugin() {

  lights.put(1, new LightModel(1, "Table Lamp", false));

  lights.put(2, new LightModel(2, "Porch light", false));

  lights.put(3, new LightModel(3, "Chandelier", true));

 }

 @DefineKernelFunction(name = "get_lights", description = "Gets a list of lights and their current state")

 public List<LightModel> getLights() {

  System.out.println("Getting lights");

  return new ArrayList<>(lights.values());

 }

 @DefineKernelFunction(name = "change_state", description = "Changes the state of the light")

 public LightModel changeState(

   @KernelFunctionParameter(name = "id", description = "The ID of the light to change") int id,

   @KernelFunctionParameter(name = "isOn", description = "The new state of the light") boolean isOn) {

  System.out.println("Changing light " + id + " " + isOn);

  if (!lights.containsKey(id)) {

   throw new IllegalArgumentException("Light not found");

  }

  lights.get(id).setIsOn(isOn);

  return lights.get(id);

 }

}

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#add-the-plugin-to-the-kernel)

#### Add the plugin to the kernel

Once you've created your plugin, you can add it to the kernel so the AI agent can access it. In the sample, we added the
`LightsPlugin` class to the kernel.

C# Copy

```

// Add the plugin to the kernel

kernel.Plugins.AddFromType<LightsPlugin>("Lights");

```

Python Copy

```

# Add the plugin to the kernel

kernel.add_plugin(

  LightsPlugin(),

  plugin_name="Lights",

)

```

Java Copy

```

// Import the LightsPlugin

KernelPlugin lightPlugin = KernelPluginFactory.createFromObject(new LightsPlugin(),

  "LightsPlugin");

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#9-planning)

### 9) Planning

Semantic Kernel leverages [function calling](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-
services/chat-completion/function-calling/)–a native feature of most LLMs–to provide
[planning](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning). With function calling, LLMs can request
(or call) a particular function to satisfy a user's request. Semantic Kernel then marshals the request to the
appropriate function in your codebase and returns the results back to the LLM so the AI agent can generate a final
response.

To enable automatic function calling, we first need to create the appropriate execution settings so that Semantic Kernel
knows to automatically invoke the functions in the kernel when the AI agent requests them.

C# Copy

```

OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new()

{

  FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()

};

```

Python Copy

```

execution_settings = AzureChatPromptExecutionSettings()

execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

```

Java Copy

```

// Enable planning

InvocationContext invocationContext = new InvocationContext.Builder()

  .withReturnMode(InvocationReturnMode.LAST_MESSAGE_ONLY)

  .withToolCallBehavior(ToolCallBehavior.allowAllKernelFunctions(true))

  .build();

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#10-invoke)

### 10) Invoke

Finally, we invoke the AI agent with the plugin. The sample code demonstrates how to generate a [non-streaming
response](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/#non-streaming-chat-
completion), but you can also generate a [streaming response](https://learn.microsoft.com/en-us/semantic-
kernel/concepts/ai-services/chat-completion/#streaming-chat-completion) by using the
`GetStreamingChatMessageContentAsync` method.

C# Copy

```

// Create chat history

var history = new ChatHistory();

// Get the response from the AI

var result = await chatCompletionService.GetChatMessageContentAsync(

  history,

  executionSettings: openAIPromptExecutionSettings,

  kernel: kernel

);

```

Run the program using this command:

Bash Copy

```

dotnet run

```

Python Copy

```

# Create a history of the conversation

history = ChatHistory()

# Get the response from the AI

result = (await chat_completion.get_chat_message_contents(

  chat_history=history,

  settings=execution_settings,

  kernel=kernel,

  arguments=KernelArguments(),

))[0]

```

Java Copy

```

userInput = scanner.nextLine();

// Add user input

history.addUserMessage(userInput);

// Prompt AI for response to users input

List<ChatMessageContent<?>> results = chatCompletionService

  .getChatMessageContentsAsync(history, kernel, invocationContext)

  .block();

```

[](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide#next-steps)

## Next steps

In this guide, you learned how to quickly get started with Semantic Kernel by building a simple AI agent that can
interact with an AI service and run your code. To see more examples and learn how to build more complex AI agents, check
out our [in-depth samples](https://learn.microsoft.com/en-us/semantic-kernel/get-started/detailed-samples).

## Additional resources

Documentation

  * [ In-depth Semantic Kernel Demos ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/detailed-samples?source=recommendations)
Go deeper with additional Demos to learn how to use Semantic Kernel.

  * [ Understanding the kernel in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel?source=recommendations)
Learn about the central component of Semantic Kernel and how it works

  * [ Supported languages for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages?source=recommendations)
Learn which features are available for C#, Python, and Java.

  * [ Introduction to Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/overview/?source=recommendations)
Learn about Semantic Kernel

  * [ Hackathon materials for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/support/hackathon-materials?source=recommendations)
Host your own Semantic Kernel hackathon with these materials.

  * [ Semantic Kernel Components ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/semantic-kernel-components?source=recommendations)
Describes the relationship between the different semantic kernel components

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

Show 4 more

Training

Module

[ Run prompts with Semantic Kernel - Training ](https://learn.microsoft.com/en-us/training/modules/create-plugins-
semantic-kernel/?source=recommendations)

This module explores Semantic Kernel SDK plugins. Learn how plugins to the SDK are used to accomplish customized tasks
and create intelligent applications.

## Additional resources

Training

Module

[ Run prompts with Semantic Kernel - Training ](https://learn.microsoft.com/en-us/training/modules/create-plugins-
semantic-kernel/?source=recommendations)

This module explores Semantic Kernel SDK plugins. Learn how plugins to the SDK are used to accomplish customized tasks
and create intelligent applications.

Documentation

  * [ In-depth Semantic Kernel Demos ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/detailed-samples?source=recommendations)
Go deeper with additional Demos to learn how to use Semantic Kernel.

  * [ Understanding the kernel in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel?source=recommendations)
Learn about the central component of Semantic Kernel and how it works

  * [ Supported languages for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages?source=recommendations)
Learn which features are available for C#, Python, and Java.

  * [ Introduction to Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/overview/?source=recommendations)
Learn about Semantic Kernel

  * [ Hackathon materials for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/support/hackathon-materials?source=recommendations)
Host your own Semantic Kernel hackathon with these materials.

  * [ Semantic Kernel Components ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/semantic-kernel-components?source=recommendations)
Describes the relationship between the different semantic kernel components

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

Show 4 more

### In this article

