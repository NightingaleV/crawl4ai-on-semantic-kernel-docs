
#### Share via

Print

Table of contents

# Task automation with agents

  * Article
  * 09/09/2024
  * 3 contributors

Feedback

## In this article

  1. [Requiring user consent](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions#requiring-user-consent)
  2. [Next steps](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions#next-steps)

Most AI agents today simply retrieve data and respond to user queries. AI agents, however, can achieve much more by
using plugins to automate tasks on behalf of users. This allows users to delegate tasks to AI agents, freeing up time
for more important work.

Once AI Agents start performing actions, however, it's important to ensure that they are acting in the best interest of
the user. This is why we provide hooks / filters to allow you to control what actions the AI agent can take.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions#requiring-user-
consent)

## Requiring user consent

When an AI agent is about to perform an action on behalf of a user, it should first ask for the user's consent. This is
especially important when the action involves sensitive data or financial transactions.

In Semantic Kernel, you can use the function invocation filter. This filter is always called whenever a function is
invoked from an AI agent. To create a filter, you need to implement the `IFunctionInvocationFilter` interface and then
add it as a service to the kernel.

Here's an example of a function invocation filter that requires user consent:

C# Copy

```

public class ApprovalFilterExample() : IFunctionInvocationFilter

{

  public async Task OnFunctionInvocationAsync(FunctionInvocationContext context, Func<FunctionInvocationContext, Task>
next)

  {

    if (context.Function.PluginName == "DynamicsPlugin" && context.Function.Name == "create_order")
    {
      Console.WriteLine("System > The agent wants to create an approval, do you want to proceed? (Y/N)");
      string shouldProceed = Console.ReadLine()!;
      if (shouldProceed != "Y")
      {
        context.Result = new FunctionResult(context.Result, "The order creation was not approved by the user");
        return;
      }
    }
    await next(context);
  }

}

```

You can then add the filter as a service to the kernel:

C# Copy

```

IKernelBuilder builder = Kernel.CreateBuilder();

builder.Services.AddSingleton<IFunctionInvocationFilter, ApprovalFilterExample>();

Kernel kernel = builder.Build();

```

Python Copy

```

from typing import Any, Coroutine

from semantic_kernel.filters.filter_types import FilterTypes

from semantic_kernel.filters.functions.function_invocation_context import FunctionInvocationContext

from semantic_kernel.functions.function_result import FunctionResult

# The `filter` decorator within kernel, creates and adds the filter in one go.

@kernel.filter(filter_type=FilterTypes.FUNCTION_INVOCATION)

async def approval_filter_example(

  context: FunctionInvocationContext, next: Coroutine[FunctionInvocationContext, Any, None]

):

  if context.function.plugin_name == "DynamicsPlugin" and context.function.name == "create_order":

    should_proceed = input("System > The agent wants to create an approval, do you want to proceed? (Y/N)")
    if should_proceed.lower() != "y":
      context.result = FunctionResult(
        function=context.function.metadata, value="The order creation was not approved by the user"
      )
      return
  await next(context)

```

> Java sample is coming soon.
Now, whenever the AI agent tries to create an order using the `DynamicsPlugin`, the user will be prompted to approve the
action.

Tip

Whenever a function is cancelled or fails, you should provide the AI agent with a meaningful error message so it can
respond appropriately. For example, if we didn't let the AI agent know that the order creation was not approved, it
would assume that the order failed due to a technical issue and would try to create the order again.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-task-automation-functions#next-steps)

## Next steps

Now that you've learned how to allow agents to automate tasks, you can learn how to allow agents to automatically create
plans to address user needs.

[Automate planning with agents](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning)

## Additional resources

Documentation

  * [ Give agents access to Logic Apps via plugins ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-logic-apps-as-plugins?source=recommendations)
Provide your workflows to agents in Semantic Kernel by adding them as plugins.

  * [ Retrieve data from plugins for RAG ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag?source=recommendations)
Learn how to statically and dynamically retrieve data from plugins for Retrieval Augmented Generation (RAG) in Semantic
Kernel.

  * [ Provide native code to your agents ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-native-plugins?source=recommendations)
Learn how to add and invoke native code as plugins in Semantic Kernel.

  * [ Give agents access to OpenAPI APIs ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?source=recommendations)
Learn how to add plugins from OpenAPI specifications to your agents in Semantic Kernel.

  * [ What are Planners in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning?source=recommendations)
Learn what a planner is in Semantic Kernel.

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

  * [ Semantic Kernel Filters ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/filters?source=recommendations)
Learn about filters in Semantic Kernel.

Show 5 more

Training

Module

[ Introduction to actions with API plugins for declarative agents - Training ](https://learn.microsoft.com/en-
us/training/modules/copilot-declarative-agent-api-plugin-intro/?source=recommendations)

Determine the scenarios for which actions for declarative agents with API plugins are suitable. Describe the function of
API plugins.

Certification

[ Microsoft Certified: Azure AI Fundamentals - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-fundamentals/?source=recommendations)

Demonstrate fundamental AI concepts related to the development of software and services of Microsoft Azure to create AI
solutions.

## Additional resources

Training

Module

[ Introduction to actions with API plugins for declarative agents - Training ](https://learn.microsoft.com/en-
us/training/modules/copilot-declarative-agent-api-plugin-intro/?source=recommendations)

Determine the scenarios for which actions for declarative agents with API plugins are suitable. Describe the function of
API plugins.

Certification

[ Microsoft Certified: Azure AI Fundamentals - Certifications ](https://learn.microsoft.com/en-
us/credentials/certifications/azure-ai-fundamentals/?source=recommendations)

Demonstrate fundamental AI concepts related to the development of software and services of Microsoft Azure to create AI
solutions.

Documentation

  * [ Give agents access to Logic Apps via plugins ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-logic-apps-as-plugins?source=recommendations)
Provide your workflows to agents in Semantic Kernel by adding them as plugins.

  * [ Retrieve data from plugins for RAG ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/using-data-retrieval-functions-for-rag?source=recommendations)
Learn how to statically and dynamically retrieve data from plugins for Retrieval Augmented Generation (RAG) in Semantic
Kernel.

  * [ Provide native code to your agents ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-native-plugins?source=recommendations)
Learn how to add and invoke native code as plugins in Semantic Kernel.

  * [ Give agents access to OpenAPI APIs ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?source=recommendations)
Learn how to add plugins from OpenAPI specifications to your agents in Semantic Kernel.

  * [ What are Planners in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning?source=recommendations)
Learn what a planner is in Semantic Kernel.

  * [ Plugins in Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?source=recommendations)
Learn how to use AI plugins in Semantic Kernel

  * [ Function calling with chat completion ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?source=recommendations)
Learn how function calling works and how to optimize your code for the best performance.

  * [ Semantic Kernel Filters ](https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/filters?source=recommendations)
Learn about filters in Semantic Kernel.

Show 5 more

### In this article

