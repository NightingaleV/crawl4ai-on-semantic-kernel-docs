# Planning

  * Article
  * 06/24/2024
  * 6 contributors

Feedback

## In this article

  1. [How does function calling create a "plan"?](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#how-does-function-calling-create-a-plan)
  2. [The automatic planning loop](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#the-automatic-planning-loop)
  3. [Using automatic function calling](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#using-automatic-function-calling)
  4. [What about the Function Calling Stepwise and Handlebars planners?](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#what-about-the-function-calling-stepwise-and-handlebars-planners)
  5. [Next steps](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#next-steps)

Once you have multiple plugins, you then need a way for your AI agent to use them together to solve a user’s need. This
is where planning comes in.

Early on, Semantic Kernel introduced the concept of planners that used prompts to request the AI to choose which
functions to invoke. Since Semantic Kernel was introduced, however, OpenAI introduced a native way for the model to
invoke or “call” a function: [function calling](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-
services/chat-completion/function-calling/). Other AI models like Gemini, Claude, and Mistral have since adopted
function calling as a core capability, making it a cross-model supported feature.

Because of these advancements, Semantic Kernel has evolved to use function calling as the primary way to plan and
execute tasks.

Important

Function calling is only available in OpenAI models that are 0613 or newer. If you use an older model (e.g., 0314), this
functionality will return an error. We recommend using the latest OpenAI models to take advantage of this feature.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#how-does-function-calling-create-a-plan)

## How does function calling create a "plan"?

At its simplest, function calling is merely a way for an AI to invoke a function with the right parameters. Take for
example a user wants to turn on a light bulb. Assuming the AI has the right plugin, it can call the function to turn on
the light.

Expand table

Role | Message  
---|---  
🔵 **User** | Please turn on light #1  
🔴 **Assistant (function call)** | `Lights.change_state(1, { "isOn": true })`  
🟢 **Tool** | `{ "id": 1, "name": "Table Lamp", "isOn": true, "brightness": 100, "hex": "FF0000" }`  
🔴 **Assistant** | The lamp is now on  
But what if the user doesn't know the ID of the light? Or what if the user wants to turn on all the lights? This is
where planning comes in. Today's LLM models are capable of iteratively calling functions to solve a user's need. This is
accomplished by creating a feedback loop where the AI can call a function, check the result, and then decide what to do
next.

For example, a user may ask the AI to "toggle" a light bulb. The AI would first need to check the state of the light
bulb before deciding whether to turn it on or off.

Expand table

Role | Message  
---|---  
🔵 **User** | Please toggle all the lights  
🔴 **Assistant (function call)** | `Lights.get_lights()`  
🟢 **Tool** | `{ "lights": [ { "id": 1, "name": "Table Lamp", "isOn": true, "brightness": 100, "hex": "FF0000" }, { "id": 2, "name": "Ceiling Light", "isOn": false, "brightness": 0, "hex": "FFFFFF" } ] }`  
🔴 **Assistant (function call)** | `Lights.change_state(1, { "isOn": false })` `Lights.change_state(2, { "isOn": true })`  
🟢 **Tool** | `{ "id": 1, "name": "Table Lamp", "isOn": false, "brightness": 0, "hex": "FFFFFF" }`  
🟢 **Tool** | `{ "id": 2, "name": "Ceiling Light", "isOn": true, "brightness": 100, "hex": "FF0000" }`  
🔴 **Assistant** | The lights have been toggled  
Note

In this example, you also saw parallel function calling. This is where the AI can call multiple functions at the same
time. This is a powerful feature that can help the AI solve complex tasks more quickly. It was added to the OpenAI
models in 1106.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#the-automatic-planning-loop)

## The automatic planning loop

Supporting function calling without Semantic Kernel is relatively complex. You would need to write a loop that would
accomplish the following:

  1. Create JSON schemas for each of your functions
  2. Provide the LLM with the previous chat history and function schemas
  3. Parse the LLM's response to determine if it wants to reply with a message or call a function
  4. If the LLM wants to call a function, you would need to parse the function name and parameters from the LLM's response
  5. Invoke the function with the right parameters
  6. Return the results of the function so that the LLM can determine what it should do next
  7. Repeat steps 2-6 until the LLM decides it has completed the task or needs help from the user

In Semantic Kernel, we make it easy to use function calling by automating this loop for you. This allows you to focus on
building the plugins needed to solve your user's needs.

Note

Understanding how the function calling loop works is essential for building performant and reliable AI agents. For an
in-depth look at how the loop works, see the [function calling](https://learn.microsoft.com/en-us/semantic-
kernel/concepts/ai-services/chat-completion/function-calling/) article.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#using-automatic-function-calling)

## Using automatic function calling

To use automatic function calling in Semantic Kernel, you need to do the following:

  1. Register the plugin with the kernel
  2. Create an execution settings object that tells the AI to automatically call functions
  3. Invoke the chat completion service with the chat history and the kernel

C# Copy

```

using System.ComponentModel;

using Microsoft.SemanticKernel;

using Microsoft.SemanticKernel.ChatCompletion;

using Microsoft.SemanticKernel.Connectors.OpenAI;

// 1. Create the kernel with the Lights plugin

var builder = Kernel.CreateBuilder().AddAzureOpenAIChatCompletion(modelId, endpoint, apiKey);

builder.Plugins.AddFromType<LightsPlugin>("Lights");

Kernel kernel = builder.Build();

var chatCompletionService = kernel.GetRequiredService<IChatCompletionService>();

// 2. Enable automatic function calling

OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new() 

{

  FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()

};

var history = new ChatHistory();

string? userInput;

do {

  // Collect user input

  Console.Write("User > ");

  userInput = Console.ReadLine();

  // Add user input

  history.AddUserMessage(userInput);

  // 3. Get the response from the AI with automatic function calling

  var result = await chatCompletionService.GetChatMessageContentAsync(

    history,
    executionSettings: openAIPromptExecutionSettings,
    kernel: kernel);
  // Print the results

  Console.WriteLine("Assistant > " + result);

  // Add the message from the agent to the chat history

  history.AddMessage(result.Role, result.Content ?? string.Empty);

} while (userInput is not null)

```

Python Copy

```

import asyncio

from semantic_kernel import Kernel

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

  # 1. Create the kernel with the Lights plugin

  kernel = Kernel()

  kernel.add_service(AzureChatCompletion(

    deployment_name="your_models_deployment_name",
    api_key="your_api_key",
    base_url="your_base_url",
  ))

  kernel.add_plugin(

    LightsPlugin(),
    plugin_name="Lights",
  )

  chat_completion : AzureChatCompletion = kernel.get_service(type=ChatCompletionClientBase)

  # 2. Enable automatic function calling

  execution_settings = AzureChatPromptExecutionSettings()

  execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

  # Create a history of the conversation

  history = ChatHistory()

  userInput = None

  while True:

    # Collect user input
    userInput = input("User > ")
    # Terminate the loop if the user says "exit"
    if userInput == "exit":
      break
    # Add user input to the history
    history.add_user_message(userInput)
    # 3. Get the response from the AI with automatic function calling
    result = (await chat_completion.get_chat_message_contents(
      chat_history=history,
      settings=execution_settings,
      kernel=kernel,
      arguments=KernelArguments(),
    ))[0]
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

When you use automatic function calling, all of the steps in the automatic planning loop are handled for you and added
to the `ChatHistory` object. After the function calling loop is complete, you can inspect the `ChatHistory` object to
see all of the function calls made and results provided by Semantic Kernel.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#what-about-the-function-calling-stepwise-and-
handlebars-planners)

## What about the Function Calling Stepwise and Handlebars planners?

The Stepwise and Handlebars planners are still available in Semantic Kernel. However, we recommend using function
calling for most tasks as it is more powerful and easier to use. Both the Stepwise and Handlebars planners will be
deprecated in a future release of Semantic Kernel.

Learn how to [migrate Stepwise Planner to Auto Function Calling](https://learn.microsoft.com/en-us/semantic-
kernel/support/migration/stepwise-planner-migration-guide).

Caution

If you are building a new AI agent, we recommend that you _not_ use the Stepwise or Handlebars planners. Instead, use
function calling as it is more powerful and easier to use.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning#next-steps)

## Next steps

Now that you understand how planners work in Semantic Kernel, you can learn more about how influence your AI agent so
that they best plan and execute tasks on behalf of your users.

## Additional resources

Documentation

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

  * [ Retrieve data from plugins for RAG ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag?source=recommendations)
Learn how to statically and dynamically retrieve data from plugins for Retrieval Augmented Generation (RAG) in Semantic
Kernel.

  * [ Give agents access to OpenAPI APIs ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?source=recommendations)
Learn how to add plugins from OpenAPI specifications to your agents in Semantic Kernel.

  * [ Provide native code to your agents ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-native-plugins?source=recommendations)
Learn how to add and invoke native code as plugins in Semantic Kernel.

  * [ Hackathon materials for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/support/hackathon-materials?source=recommendations)
Host your own Semantic Kernel hackathon with these materials.

  * [ Allow agents to automate tasks ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions?source=recommendations)
Learn how you safely allow agents to automate tasks on behalf of users in Semantic Kernel.

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

Show 4 more

Training

Module

[ Automatic function calling - Training ](https://learn.microsoft.com/en-us/training/modules/automatic-function-
calling/?source=recommendations)

Learn how you can automatically invoke functions using the Semantic Kernel SDK.

## Additional resources

Training

Module

[ Automatic function calling - Training ](https://learn.microsoft.com/en-us/training/modules/automatic-function-
calling/?source=recommendations)

Learn how you can automatically invoke functions using the Semantic Kernel SDK.

Documentation

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

  * [ Retrieve data from plugins for RAG ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag?source=recommendations)
Learn how to statically and dynamically retrieve data from plugins for Retrieval Augmented Generation (RAG) in Semantic
Kernel.

  * [ Give agents access to OpenAPI APIs ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?source=recommendations)
Learn how to add plugins from OpenAPI specifications to your agents in Semantic Kernel.

  * [ Provide native code to your agents ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-native-plugins?source=recommendations)
Learn how to add and invoke native code as plugins in Semantic Kernel.

  * [ Hackathon materials for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/support/hackathon-materials?source=recommendations)
Host your own Semantic Kernel hackathon with these materials.

  * [ Allow agents to automate tasks ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions?source=recommendations)
Learn how you safely allow agents to automate tasks on behalf of users in Semantic Kernel.

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

Show 4 more

### In this article

