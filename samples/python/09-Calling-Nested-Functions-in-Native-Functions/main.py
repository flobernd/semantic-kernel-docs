import semantic_kernel as sk
from plugins.MathPlugin.Math import Math
from plugins.OrchestratorPlugin.Orchestrator import Orchestrator
from semantic_kernel.core_skills import ConversationSummaryPlugin
import config.add_completion_service


async def main():
    # Initialize the kernel
    kernel = sk.Kernel()
    # Add a text or chat completion service using either:
    # kernel.add_text_completion_service()
    # kernel.add_chat_service()
    kernel.add_completion_service()

    plugins_directory = "./plugins"

    # Import the semantic functions
    kernel.import_semantic_skill_from_directory(plugins_directory, "OrchestratorPlugin")
    kernel.import_skill(
        ConversationSummaryPlugin(kernel=kernel), skill_name="ConversationSummaryPlugin"
    )

    # Import the native functions.
    math_plugin = kernel.import_skill(Math(), skill_name="MathPlugin")
    orchestrator_plugin = kernel.import_skill(
        Orchestrator(kernel), skill_name="OrchestratorPlugin"
    )

    # Make a request that runs the Sqrt function.
    result1 = await kernel.run_async(
        orchestrator_plugin["RouteRequest"],
        input_str="What is the square root of 634?",
    )
    print(result1)

    # Make a request that runs the Multiply function.
    result2 = await kernel.run_async(
        orchestrator_plugin["RouteRequest"],
        input_str="What is 12.34 times 56.78?",
    )
    print(result2)


# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
