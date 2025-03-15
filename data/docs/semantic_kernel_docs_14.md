
# Experimental Features in Semantic Kernel

  * Article
  * 03/06/2025
  * 1 contributor

Feedback

## In this article

  1. [Purpose of Experimental Features](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#purpose-of-experimental-features)
  2. [Implications for Users](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#implications-for-users)
  3. [Using Experimental Features in .NET](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#using-experimental-features-in-net)
  4. [Developing and Contributing to Experimental Features](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#developing-and-contributing-to-experimental-features)
  5. [Future of Experimental Features](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#future-of-experimental-features)
  6. [Getting Involved](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#getting-involved)
  7. [Summary](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#summary)

Show 3 more

Semantic Kernel introduces experimental features to provide early access to new, evolving capabilities. These features
allow users to explore cutting-edge functionality, but they are not yet stable and may be modified, deprecated, or
removed in future releases.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#purpose-of-experimental-features)

## Purpose of Experimental Features

The `Experimental` attribute serves several key purposes:

  * **Signals Instability** – Indicates that a feature is still evolving and not yet production-ready.
  * **Encourages Early Feedback** – Allows developers to test and provide input before a feature is fully stabilized.
  * **Manages Expectations** – Ensures users understand that experimental features may have limited support or documentation.
  * **Facilitates Rapid Iteration** – Enables the team to refine and improve features based on real-world usage.
  * **Guides Contributors** – Helps maintainers and contributors recognize that the feature is subject to significant changes.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#implications-for-users)

## Implications for Users

Using experimental features comes with certain considerations:

  * **Potential Breaking Changes** – APIs, behavior, or entire features may change without prior notice.
  * **Limited Support** – The Semantic Kernel team may provide limited or no support for experimental features.
  * **Stability Concerns** – Features may be less stable and prone to unexpected behavior or performance issues.
  * **Incomplete Documentation** – Experimental features may have incomplete or outdated documentation.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#suppressing-experimental-feature-
warnings-in-net)

### Suppressing Experimental Feature Warnings in .NET

In the .NET SDK, experimental features generate compiler warnings. To suppress these warnings in your project, add the
relevant diagnostic IDs to your `.csproj` file:

XML Copy

```

<PropertyGroup>

 <NoWarn>$(NoWarn);SKEXP0001,SKEXP0010</NoWarn>

</PropertyGroup>

```

Each experimental feature has a unique diagnostic code (`SKEXPXXXX`). The full list can be found in .

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#using-experimental-features-in-net)

## Using Experimental Features in .NET

In .NET, experimental features are marked using the `[Experimental]` attribute:

C# Copy

```

using System;

using System.Diagnostics.CodeAnalysis;

[Experimental("SKEXP0101", "FeatureCategory")]

public class NewFeature

{

  public void ExperimentalMethod()

  {

    Console.WriteLine("This is an experimental feature.");
  }

}

```

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#experimental-feature-support-in-
other-sdks)

### Experimental Feature Support in Other SDKs

  * **Python and Java** do not have a built-in experimental feature system like .NET.
  * Experimental features in **Python** may be marked using warnings (e.g., `warnings.warn`).
  * In **Java** , developers typically use custom annotations to indicate experimental features.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#developing-and-contributing-to-
experimental-features)

## Developing and Contributing to Experimental Features

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#marking-a-feature-as-experimental)

### Marking a Feature as Experimental

  * Apply the `Experimental` attribute to classes, methods, or properties:

C# Copy

```

[Experimental("SKEXP0101", "FeatureCategory")]

public class NewFeature { }

```

  * Include a brief description explaining why the feature is experimental.
  * Use meaningful tags as the second argument to categorize and track experimental features.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#coding-and-documentation-best-
practices)

### Coding and Documentation Best Practices

  * **Follow Coding Standards** – Maintain Semantic Kernel's coding conventions.
  * **Write Unit Tests** – Ensure basic functionality and prevent regressions.
  * **Document All Changes** – Update relevant documentation, including `EXPERIMENTS.md`.
  * **Use GitHub for Discussions** – Open issues or discussions to gather feedback.
  * **Consider Feature Flags** – Where appropriate, use feature flags to allow opt-in/opt-out.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#communicating-changes)

### Communicating Changes

  * Clearly document updates, fixes, or breaking changes.
  * Provide migration guidance if the feature is evolving.
  * Tag the relevant GitHub issues for tracking progress.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#future-of-experimental-features)

## Future of Experimental Features

Experimental features follow one of three paths:

  1. **Graduation to Stable** – If a feature is well-received and technically sound, it may be promoted to stable.
  2. **Deprecation & Removal** – Features that do not align with long-term goals may be removed.
  3. **Continuous Experimentation** – Some features may remain experimental indefinitely while being iterated upon.

The Semantic Kernel team strives to communicate experimental feature updates through release notes and documentation
updates.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#getting-involved)

## Getting Involved

The community plays a crucial role in shaping the future of experimental features. Provide feedback via:

  * **GitHub Issues** – Report bugs, request improvements, or share concerns.
  * **Discussions & PRs** – Engage in discussions and contribute directly to the codebase.

[](https://learn.microsoft.com/en-us/semantic-kernel/concepts/experimental-attribute#summary)

## Summary

  * **Experimental features** allow users to test and provide feedback on new capabilities in Semantic Kernel.
  * **They may change frequently** , have limited support, and require caution when used in production.
  * **Contributors should follow best practices** , use `[Experimental]` correctly, and document changes properly.
  * **Users can suppress warnings** for experimental features but should stay updated on their evolution.

For the latest details, check .

## Additional resources

Documentation

  * [ Kernel Events and Filters Migration ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/kernel-events-and-filters-migration?source=recommendations)
Describes the steps for SK caller code to migrate from Kernel Events and use latest version of Filters

  * [ Migrating from Memory Stores to Vector Stores ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/memory-store-migration?source=recommendations)
Describes how to migrate from using memory stores to vector stores in semantic kernel.

  * [ .NET Migrating from Stepwise Planner to Auto Function Calling ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/stepwise-planner-migration-guide?source=recommendations)
Describes the steps for SK caller code to migrate from Stepwise Planner to Auto Function Calling.

  * [ Upgrading to v1+ of the .NET Semantic Kernel SDK ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/v1-migration-guide?source=recommendations)
Learn how to upgrade from a pre-v1 version of the .NET Semantic Kernel SDK to v1+.

  * [ Security ](https://learn.microsoft.com/en-us/semantic-kernel/support/security?source=recommendations)
  * [ Glossary for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/support/glossary?source=recommendations)
Glossary for Semantic Kernel

Show 3 more

Training

Module

[ Build your kernel - Training ](https://learn.microsoft.com/en-us/training/modules/build-your-
kernel/?source=recommendations)

Learn how the semantic kernel SDK connects native code to large language models to create smart applications.

## Additional resources

Training

Module

[ Build your kernel - Training ](https://learn.microsoft.com/en-us/training/modules/build-your-
kernel/?source=recommendations)

Learn how the semantic kernel SDK connects native code to large language models to create smart applications.

Documentation

  * [ Kernel Events and Filters Migration ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/kernel-events-and-filters-migration?source=recommendations)
Describes the steps for SK caller code to migrate from Kernel Events and use latest version of Filters

  * [ Migrating from Memory Stores to Vector Stores ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/memory-store-migration?source=recommendations)
Describes how to migrate from using memory stores to vector stores in semantic kernel.

  * [ .NET Migrating from Stepwise Planner to Auto Function Calling ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/stepwise-planner-migration-guide?source=recommendations)
Describes the steps for SK caller code to migrate from Stepwise Planner to Auto Function Calling.

  * [ Upgrading to v1+ of the .NET Semantic Kernel SDK ](https://learn.microsoft.com/en-us/semantic-kernel/support/migration/v1-migration-guide?source=recommendations)
Learn how to upgrade from a pre-v1 version of the .NET Semantic Kernel SDK to v1+.

  * [ Security ](https://learn.microsoft.com/en-us/semantic-kernel/support/security?source=recommendations)
  * [ Glossary for Semantic Kernel ](https://learn.microsoft.com/en-us/semantic-kernel/support/glossary?source=recommendations)
Glossary for Semantic Kernel

Show 3 more

### In this article

