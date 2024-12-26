Text generation
===============

Learn how to generate text from a prompt.

OpenAI provides simple APIs to use a [large language model](/docs/models) to generate text from a prompt, as you might using [ChatGPT](https://chatgpt.com). These models have been trained on vast quantities of data to understand multimedia inputs and natural language instructions. From these [prompts](/docs/guides/prompt-engineering), models can generate almost any kind of text response, like code, mathematical equations, structured JSON data, or human-like prose.

Quickstart
----------

To generate text, you can use the [chat completions endpoint](/docs/api-reference/chat/) in the REST API, as seen in the examples below. You can either use the [REST API](/docs/api-reference) from the HTTP client of your choice, or use one of OpenAI's [official SDKs](/docs/libraries) for your preferred programming language.

Generate prose

Create a human-like response to a prompt

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
        { role: "developer", content: "You are a helpful assistant." },
        {
            role: "user",
            content: "Write a haiku about recursion in programming.",
        },
    ],
});

console.log(completion.choices[0].message);
```

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
```

```bash
curl "https://api.openai.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-4o",
        "messages": [
            {
                "role": "developer",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    }'
```

Analyze an image

Describe the contents of an image

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
        {
            role: "user",
            content: [
                { type: "text", text: "What's in this image?" },
                {
                    type: "image_url",
                    image_url: {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                }
            ],
        },
    ],
});

console.log(completion.choices[0].message);
```

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    }
                },
            ],
        }
    ],
)

print(completion.choices[0].message)
```

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
          }
        ]
      }
    ]
  }'
```

Generate JSON data

Generate JSON data based on a JSON Schema

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const completion = await openai.chat.completions.create({
    model: "gpt-4o-2024-08-06",
    messages: [
        { role: "developer", content: "You extract email addresses into JSON data." },
        {
            role: "user",
            content: "Feeling stuck? Send a message to help@mycompany.com.",
        },
    ],
    response_format: {
        // See /docs/guides/structured-outputs
        type: "json_schema",
        json_schema: {
            name: "email_schema",
            schema: {
                type: "object",
                properties: {
                    email: {
                        description: "The email address that appears in the input",
                        type: "string"
                    }
                },
                additionalProperties: false
            }
        }
    }
});

console.log(completion.choices[0].message.content);
```

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
        {
            "role": "developer", 
            "content": "You extract email addresses into JSON data."
        },
        {
            "role": "user", 
            "content": "Feeling stuck? Send a message to help@mycompany.com."
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "email_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "email": {
                        "description": "The email address that appears in the input",
                        "type": "string"
                    },
                    "additionalProperties": False
                }
            }
        }
    }
)

print(response.choices[0].message.content);
```

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-2024-08-06",
    "messages": [
      {
        "role": "developer",
        "content": "You extract email addresses into JSON data."
      },
      {
        "role": "user",
        "content": "Feeling stuck? Send a message to help@mycompany.com."
      }
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "email_schema",
        "schema": {
            "type": "object",
            "properties": {
                "email": {
                    "description": "The email address that appears in the input",
                    "type": "string"
                }
            },
            "additionalProperties": false
        }
      }
    }
  }'
```

Choosing a model
----------------

When making a text generation request, the first option to configure is which [model](/docs/models) you want to generate the response. The model you choose can greatly influence the output, and impact how much each generation request [costs](https://openai.com/api/pricing/).

*   A **large model** like [`gpt-4o`](/docs/models#gpt-4o) will offer a very high level of intelligence and strong performance, while having a higher cost per token.
*   A **small model** like [`gpt-4o-mini`](/docs/models#gpt-4o-mini) offers intelligence not quite on the level of the larger model, but is faster and less expensive per token.
*   A **reasoning model** like [the `o1` family of models](/docs/models#o1) is slower to return a result, and uses more tokens to "think", but is capable of advanced reasoning, coding, and multi-step planning.

Experiment with different models [in the Playground](/playground) to see which one works best for your prompts! More information on choosing a model can [also be found here](/docs/guides/model-selection).

Building prompts
----------------

The process of crafting prompts to get the right output from a model is called **prompt engineering**. By giving the model precise instructions, examples, and necessary context information (like private or specialized information that wasn't included in the model's training data), you can improve the quality and accuracy of the model's output. Here, we'll get into some high-level guidance on building prompts, but you might also find the [prompt engineering guide](/docs/guides/prompt-engineering) helpful.

In the [chat completions](/docs/api-reference/chat/) API, you create prompts by providing an array of `messages` that contain instructions for the model. Each message can have a different `role`, which influences how the model might interpret the input.

### User messages

User messages contain instructions that request a particular type of output from the model. You can think of `user` messages as the messages you might type in to [ChatGPT](https://chaptgpt.com) as an end user.

Here's an example of a user message prompt that asks the `gpt-4o` model to generate a haiku poem based on a prompt.

```javascript
const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Write a haiku about programming."
        }
      ]
    }
  ]
});
```

### Developer messages

Messages with the `developer` role provide instructions to the model that are prioritized ahead of user messages, as described in the [chain of command section in the model spec](https://cdn.openai.com/spec/model-spec-2024-05-08.html#follow-the-chain-of-command). They typically describe how the model should generally behave and respond. This message role used to be called the `system` prompt, but it has been renamed to more accurately describe its place in the instruction-following hierarchy.

Here's an example of a developer message that modifies the behavior of the model when generating a response to a `user` message:

```javascript
const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    {
      "role": "developer",
      "content": [
        {
          "type": "text",
          "text": `
            You are a helpful assistant that answers programming 
            questions in the style of a southern belle from the 
            southeast United States.
          `
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Are semicolons optional in JavaScript?"
        }
      ]
    }
  ]
});
```

This prompt returns a text output in the rhetorical style requested:

```text
Well, sugar, that's a fine question you've got there! Now, in the 
world of JavaScript, semicolons are indeed a bit like the pearls 
on a necklace – you might slip by without 'em, but you sure do look 
more polished with 'em in place. 

Technically, JavaScript has this little thing called "automatic 
semicolon insertion" where it kindly adds semicolons for you 
where it thinks they oughta go. However, it's not always perfect, 
bless its heart. Sometimes, it might get a tad confused and cause 
all sorts of unexpected behavior.
```

### Assistant messages

Messages with the `assistant` role are presumed to have been generated by the model, perhaps in a previous generation request (see the "Conversations" section below). They can also be used to provide examples to the model for how it should respond to the current request - a technique known as **few-shot learning**.

Here's an example of using an assistant message to capture the results of a previous text generation result, and making a new request based on that.

```javascript
const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    {
      "role": "user",
      "content": [{ "type": "text", "text": "knock knock." }]
    },
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "Who's there?" }]
    },
    {
      "role": "user",
      "content": [{ "type": "text", "text": "Orange." }]
    }
  ]
});
```

### Giving the model additional data to use for generation

The message types above can also be used to provide additional information to the model which may be outside its training data. You might want to include the results of a database query, a text document, or other resources to help the model generate a relevant response. This technique is often referred to as **retrieval augmented generation**, or RAG. [Learn more about RAG techniques here](https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts).

Conversations and context
-------------------------

While each text generation request is independent and stateless (unless you are using [assistants](/docs/assistants/overview)), you can still implement **multi-turn conversations** by providing additional messages as parameters to your text generation request. Consider the "knock knock" joke example shown above:

```javascript
const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    {
      "role": "user",
      "content": [{ "type": "text", "text": "knock knock." }]
    },
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "Who's there?" }]
    },
    {
      "role": "user",
      "content": [{ "type": "text", "text": "Orange." }]
    }
  ]
});
```

By using alternating `user` and `assistant` messages, you can capture the previous state of a conversation in one request to the model.

### Managing context for text generation

As your inputs become more complex, or you include more and more turns in a conversation, you will need to consider both **output token** and **context window** limits. Model inputs and outputs are metered in [**tokens**](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them), which are parsed from inputs to analyze their content and intent, and assembled to render logical outputs. Models have limits on how many tokens can be used during the lifecycle of a text generation request.

*   **Output tokens** are the tokens that are generated by a model in response to a prompt. Each model supports different limits for output tokens, [documented here](/docs/models). For example, `gpt-4o-2024-08-06` can generate a maximum of 16,384 output tokens.
*   A **context window** describes the total tokens that can be used for both input tokens and output tokens (and for some models, [reasoning tokens](/docs/guides/reasoning)), [documented here](/docs/models). For example, `gpt-4o-2024-08-06` has a total context window of 128k tokens.

If you create a very large prompt (usually by including a lot of conversation context or additional data/examples for the model), you run the risk of exceeding the allocated context window for a model, which might result in truncated outputs.

You can use the [tokenizer tool](/tokenizer) (which uses the [tiktoken library](https://github.com/openai/tiktoken)) to see how many tokens are present in a string of text.

Optimizing model outputs
------------------------

As you iterate on your prompts, you will be continually trying to improve **accuracy**, **cost**, and **latency**.

||
|Accuracy|Ensure the model produces accurate and useful responses to your prompts.|Accurate responses require that the model has all the information it needs to generate a response, and knows how to go about creating a response (from interpreting input to formatting and styling). Often, this will require a mix of prompt engineering, RAG, and model fine-tuning.Learn about optimizing for accuracy here.|
|Cost|Drive down the total cost of model usage by reducing token usage and using cheaper models when possible.|To control costs, you can try to use fewer tokens or smaller, cheaper models. Learn more about optimizing for cost here.|
|Latency|Decrease the time it takes to generate responses to your prompts.|Optimizing latency is a multi-faceted process including prompt engineering, parallelism in your own code, and more. Learn more here.|

Next steps
----------

There's much more to explore in text generation - here's a few resources to go even deeper.

[

Prompt examples

Get inspired by example prompts for a variety of use cases.

](/docs/examples)[

Build a prompt in the Playground

Use the Playground to develop and iterate on prompts.

](/playground)[

Browse the Cookbook

The Cookbook has complex examples covering a variety of use cases.

](/docs/guides/https://cookbook.openai.com)[

Generate JSON data with Structured Outputs

Ensure JSON data emitted from a model conforms to a JSON schema.

](/docs/guides/structured-outputs)[

Full API reference

Check out all the options for text generation in the API reference.

](/docs/api-reference/chat)
Structured Outputs
==================

Ensure responses adhere to a JSON schema.

Try it out
----------

Try it out in the [Playground](/playground) or generate a ready-to-use schema definition to experiment with structured outputs.

Generate

Introduction
------------

JSON is one of the most widely used formats in the world for applications to exchange data.

Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied [JSON Schema](https://json-schema.org/overview/what-is-jsonschema), so you don't need to worry about the model omitting a required key, or hallucinating an invalid enum value.

Some benefits of Structured Outputs include:

1.  **Reliable type-safety:** No need to validate or retry incorrectly formatted responses
2.  **Explicit refusals:** Safety-based model refusals are now programmatically detectable
3.  **Simpler prompting:** No need for strongly worded prompts to achieve consistent formatting

In addition to supporting JSON Schema in the REST API, the OpenAI SDKs for [Python](https://github.com/openai/openai-python/blob/main/helpers.md#structured-outputs-parsing-helpers) and [JavaScript](https://github.com/openai/openai-node/blob/master/helpers.md#structured-outputs-parsing-helpers) also make it easy to define object schemas using [Pydantic](https://docs.pydantic.dev/latest/) and [Zod](https://zod.dev/) respectively. Below, you can see how to extract information from unstructured text that conforms to a schema defined in code.

Getting a structured response

```javascript
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI();

const CalendarEvent = z.object({
  name: z.string(),
  date: z.string(),
  participants: z.array(z.string()),
});

const completion = await openai.beta.chat.completions.parse({
  model: "gpt-4o-2024-08-06",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "Alice and Bob are going to a science fair on Friday." },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
```

```python
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed
```

### Supported models

Structured Outputs are available in our [latest large language models](/docs/models), starting with GPT-4o:

*   `o1-2024-12-17` and later
*   `gpt-4o-mini-2024-07-18` and later
*   `gpt-4o-2024-08-06` and later

Older models like `gpt-4-turbo` and earlier may use [JSON mode](#json-mode) instead.

When to use Structured Outputs via function calling vs via response\_format

-------------------------------------------------------------------------------

Structured Outputs is available in two forms in the OpenAI API:

1.  When using [function calling](/docs/guides/function-calling)
2.  When using a `json_schema` response format

Function calling is useful when you are building an application that bridges the models and functionality of your application.

For example, you can give the model access to functions that query a database in order to build an AI assistant that can help users with their orders, or functions that can interact with the UI.

Conversely, Structured Outputs via `response_format` are more suitable when you want to indicate a structured schema for use when the model responds to the user, rather than when the model calls a tool.

For example, if you are building a math tutoring application, you might want the assistant to respond to your user using a specific JSON Schema so that you can generate a UI that displays different parts of the model's output in distinct ways.

Put simply:

*   If you are connecting the model to tools, functions, data, etc. in your system, then you should use function calling
*   If you want to structure the model's output when it responds to the user, then you should use a structured `response_format`

The remainder of this guide will focus on non-function calling use cases in the Chat Completions API. To learn more about how to use Structured Outputs with function calling, check out the [Function Calling](/docs/guides/function-calling#function-calling-with-structured-outputs) guide.

### Structured Outputs vs JSON mode

Structured Outputs is the evolution of [JSON mode](#json-mode). While both ensure valid JSON is produced, only Structured Outputs ensure schema adherance. Both Structured Outputs and JSON mode are supported in the Chat Completions API, Assistants API, Fine-tuning API and Batch API.

We recommend always using Structured Outputs instead of JSON mode when possible.

However, Structured Outputs with `response_format: {type: "json_schema", ...}` is only supported with the `gpt-4o-mini`, `gpt-4o-mini-2024-07-18`, and `gpt-4o-2024-08-06` model snapshots and later.

||Structured Outputs|JSON Mode|
|---|---|---|
|Outputs valid JSON|Yes|Yes|
|Adheres to schema|Yes (see supported schemas)|No|
|Compatible models|gpt-4o-mini, gpt-4o-2024-08-06, and later|gpt-3.5-turbo, gpt-4-* and gpt-4o-* models|
|Enabling|response_format: { type: "json_schema", json_schema: {"strict": true, "schema": ...} }|response_format: { type: "json_object" }|

Examples
--------

Chain of thoughtStructured data extractionUI generationModeration

### Chain of thought

You can ask the model to output an answer in a structured, step-by-step way, to guide the user through the solution.

Structured Outputs for chain-of-thought math tutoring

```javascript
import OpenAI from "openai";
import { z } from "zod";
import { zodResponseFormat } from "openai/helpers/zod";

const openai = new OpenAI();

const Step = z.object({
  explanation: z.string(),
  output: z.string(),
});

const MathReasoning = z.object({
  steps: z.array(Step),
  final_answer: z.string(),
});

const completion = await openai.beta.chat.completions.parse({
  model: "gpt-4o-2024-08-06",
  messages: [
    { role: "system", content: "You are a helpful math tutor. Guide the user through the solution step by step." },
    { role: "user", content: "how can I solve 8x + 7 = -23" },
  ],
  response_format: zodResponseFormat(MathReasoning, "math_reasoning"),
});

const math_reasoning = completion.choices[0].message.parsed;
```

```python
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "how can I solve 8x + 7 = -23"}
    ],
    response_format=MathReasoning,
)

math_reasoning = completion.choices[0].message.parsed
```

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-2024-08-06",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful math tutor. Guide the user through the solution step by step."
      },
      {
        "role": "user",
        "content": "how can I solve 8x + 7 = -23"
      }
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "math_reasoning",
        "schema": {
          "type": "object",
          "properties": {
            "steps": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "explanation": { "type": "string" },
                  "output": { "type": "string" }
                },
                "required": ["explanation", "output"],
                "additionalProperties": false
              }
            },
            "final_answer": { "type": "string" }
          },
          "required": ["steps", "final_answer"],
          "additionalProperties": false
        },
        "strict": true
      }
    }
  }'
```

#### Example response

```json
{
  "steps": [
    {
      "explanation": "Start with the equation 8x + 7 = -23.",
      "output": "8x + 7 = -23"
    },
    {
      "explanation": "Subtract 7 from both sides to isolate the term with the variable.",
      "output": "8x = -23 - 7"
    },
    {
      "explanation": "Simplify the right side of the equation.",
      "output": "8x = -30"
    },
    {
      "explanation": "Divide both sides by 8 to solve for x.",
      "output": "x = -30 / 8"
    },
    {
      "explanation": "Simplify the fraction.",
      "output": "x = -15 / 4"
    }
  ],
  "final_answer": "x = -15 / 4"
}
```

How to use Structured Outputs with response\_format

-------------------------------------------------------

You can use Structured Outputs with the new SDK helper to parse the model's output into your desired format, or you can specify the JSON schema directly.

**Note:** the first request you make with any schema will have additional latency as our API processes the schema, but subsequent requests with the same schema will not have additional latency.

SDK objectsManual schema

Step 1: Define your object

First you must define an object or data structure to represent the JSON Schema that the model should be constrained to follow. See the [examples](/docs/guides/structured-outputs#examples) at the top of this guide for reference.

While Structured Outputs supports much of JSON Schema, some features are unavailable either for performance or technical reasons. See [here](/docs/guides/structured-outputs#supported-schemas) for more details.

For example, you can define an object like this:

```python
from pydantic import BaseModel

class Step(BaseModel):
  explanation: str
  output: str

class MathResponse(BaseModel):
  steps: list[Step]
  final_answer: str
```

```javascript
import { z } from "zod";
import { zodResponseFormat } from "openai/helpers/zod";

const Step = z.object({
explanation: z.string(),
output: z.string(),
});

const MathResponse = z.object({
steps: z.array(Step),
final_answer: z.string(),
});
```

#### Tips for your data structure

To maximize the quality of model generations, we recommend the following:

*   Name keys clearly and intuitively
*   Create clear titles and descriptions for important keys in your structure
*   Create and use evals to determine the structure that works best for your use case

Step 2: Supply your object in the API call

You can use the `parse` method to automatically parse the JSON response into the object you defined.

Under the hood, the SDK takes care of supplying the JSON schema corresponding to your data structure, and then parsing the response as an object.

```python
completion = client.beta.chat.completions.parse(
  model="gpt-4o-2024-08-06",
  messages=[
      {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
      {"role": "user", "content": "how can I solve 8x + 7 = -23"}
  ],
  response_format=MathResponse
)
```

```javascript
const completion = await openai.beta.chat.completions.parse({
model: "gpt-4o-2024-08-06",
messages: [
  { role: "system", content: "You are a helpful math tutor. Guide the user through the solution step by step." },
  { role: "user", content: "how can I solve 8x + 7 = -23" },
],
response_format: zodResponseFormat(MathResponse, "math_response"),
});
```

Step 3: Handle edge cases

In some cases, the model might not generate a valid response that matches the provided JSON schema.

This can happen in the case of a refusal, if the model refuses to answer for safety reasons, or if for example you reach a max tokens limit and the response is incomplete.

```python
try:
  completion = client.beta.chat.completions.parse(
      model="gpt-4o-2024-08-06",
      messages=[
          {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
          {"role": "user", "content": "how can I solve 8x + 7 = -23"}
      ],
      response_format=MathResponse,
      max_tokens=50
  )
  math_response = completion.choices[0].message
  if math_response.parsed:
      print(math_response.parsed)
  elif math_response.refusal:
      # handle refusal
      print(math_response.refusal)
except Exception as e:
  # Handle edge cases
  if type(e) == openai.LengthFinishReasonError:
      # Retry with a higher max tokens
      print("Too many tokens: ", e)
      pass
  else:
      # Handle other exceptions
      print(e)
      pass
```

```javascript
try {
const completion = await openai.beta.chat.completions.parse({
  model: "gpt-4o-2024-08-06",
  messages: [
    {
      role: "system",
      content:
        "You are a helpful math tutor. Guide the user through the solution step by step.",
    },
    { role: "user", content: "how can I solve 8x + 7 = -23" },
  ],
  response_format: zodResponseFormat(MathResponse, "math_response"),
  max_tokens: 50,
});

const math_response = completion.choices[0].message;
console.log(math_response);
if (math_response.parsed) {
  console.log(math_response.parsed);
} else if (math_response.refusal) {
  // handle refusal
  console.log(math_response.refusal);
}
} catch (e) {
// Handle edge cases
if (e.constructor.name == "LengthFinishReasonError") {
  // Retry with a higher max tokens
  console.log("Too many tokens: ", e.message);
} else {
  // Handle other exceptions
  console.log("An error occurred: ", e.message);
}
}
```

Step 4: Use the generated structured data in a type-safe way

When using the SDK, you can use the `parsed` attribute to access the parsed JSON response as an object. This object will be of the type you defined in the `response_format` parameter.

```python
math_response = completion.choices[0].message.parsed
print(math_response.steps)
print(math_response.final_answer)
```

```javascript
const math_response = completion.choices[0].message.parsed;
console.log(math_response.steps);
console.log(math_response.final_answer);
```

### 

Refusals with Structured Outputs

When using Structured Outputs with user-generated input, OpenAI models may occasionally refuse to fulfill the request for safety reasons. Since a refusal does not necessarily follow the schema you have supplied in `response_format`, the API response will include a new field called `refusal` to indicate that the model refused to fulfill the request.

When the `refusal` property appears in your output object, you might present the refusal in your UI, or include conditional logic in code that consumes the response to handle the case of a refused request.

```python
class Step(BaseModel):
  explanation: str
  output: str

class MathReasoning(BaseModel):
  steps: list[Step]
  final_answer: str

completion = client.beta.chat.completions.parse(
  model="gpt-4o-2024-08-06",
  messages=[
      {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
      {"role": "user", "content": "how can I solve 8x + 7 = -23"}
  ],
  response_format=MathReasoning,
)

math_reasoning = completion.choices[0].message

# If the model refuses to respond, you will get a refusal message
if (math_reasoning.refusal):
  print(math_reasoning.refusal)
else:
  print(math_reasoning.parsed)
```

```javascript
const Step = z.object({
explanation: z.string(),
output: z.string(),
});

const MathReasoning = z.object({
steps: z.array(Step),
final_answer: z.string(),
});

const completion = await openai.beta.chat.completions.parse({
model: "gpt-4o-2024-08-06",
messages: [
  { role: "system", content: "You are a helpful math tutor. Guide the user through the solution step by step." },
  { role: "user", content: "how can I solve 8x + 7 = -23" },
],
response_format: zodResponseFormat(MathReasoning, "math_reasoning"),
});

const math_reasoning = completion.choices[0].message

// If the model refuses to respond, you will get a refusal message
if (math_reasoning.refusal) {
console.log(math_reasoning.refusal);
} else {
console.log(math_reasoning.parsed);
}
```

The API response from a refusal will look something like this:

```json
{
"id": "chatcmpl-9nYAG9LPNonX8DAyrkwYfemr3C8HC",
"object": "chat.completion",
"created": 1721596428,
"model": "gpt-4o-2024-08-06",
"choices": [
  {
  "index": 0,
  "message": {
          "role": "assistant",
          "refusal": "I'm sorry, I cannot assist with that request."
  },
  "logprobs": null,
  "finish_reason": "stop"
}
],
"usage": {
    "prompt_tokens": 81,
    "completion_tokens": 11,
    "total_tokens": 92,
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
},
"system_fingerprint": "fp_3407719c7f"
}
```

### 

Tips and best practices

#### Handling user-generated input

If your application is using user-generated input, make sure your prompt includes instructions on how to handle situations where the input cannot result in a valid response.

The model will always try to adhere to the provided schema, which can result in hallucinations if the input is completely unrelated to the schema.

You could include language in your prompt to specify that you want to return empty parameters, or a specific sentence, if the model detects that the input is incompatible with the task.

#### Handling mistakes

Structured Outputs can still contain mistakes. If you see mistakes, try adjusting your instructions, providing examples in the system instructions, or splitting tasks into simpler subtasks. Refer to the [prompt engineering guide](/docs/guides/prompt-engineering) for more guidance on how to tweak your inputs.

#### Avoid JSON schema divergence

To prevent your JSON Schema and corresponding types in your programming language from diverging, we strongly recommend using the native Pydantic/zod sdk support.

If you prefer to specify the JSON schema directly, you could add CI rules that flag when either the JSON schema or underlying data objects are edited, or add a CI step that auto-generates the JSON Schema from type definitions (or vice-versa).

Streaming
---------

You can use streaming to process model responses or function call arguments as they are being generated, and parse them as structured data.

That way, you don't have to wait for the entire response to complete before handling it. This is particularly useful if you would like to display JSON fields one by one, or handle function call arguments as soon as they are available.

We recommend relying on the SDKs to handle streaming with Structured Outputs. You can find an example of how to stream function call arguments without the SDK `stream` helper in the [function calling guide](/docs/guides/function-calling#advanced-usage).

Here is how you can stream a model response with the `stream` helper:

```python
from typing import List
from pydantic import BaseModel
from openai import OpenAI

class EntitiesModel(BaseModel):
  attributes: List[str]
  colors: List[str]
  animals: List[str]

client = OpenAI()

with client.beta.chat.completions.stream(
  model="gpt-4o",
  messages=[
      {"role": "system", "content": "Extract entities from the input text"},
      {
          "role": "user",
          "content": "The quick brown fox jumps over the lazy dog with piercing blue eyes",
      },
  ],
  response_format=EntitiesModel,
) as stream:
  for event in stream:
      if event.type == "content.delta":
          if event.parsed is not None:
              # Print the parsed data as JSON
              print("content.delta parsed:", event.parsed)
      elif event.type == "content.done":
          print("content.done")
      elif event.type == "error":
          print("Error in stream:", event.error)

final_completion = stream.get_final_completion()
print("Final completion:", final_completion)
```

```js
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";
export const openai = new OpenAI();

const EntitiesSchema = z.object({
attributes: z.array(z.string()),
colors: z.array(z.string()),
animals: z.array(z.string()),
});

const stream = openai.beta.chat.completions
.stream({
  model: "gpt-4o",
  messages: [
    { role: "system", content: "Extract entities from the input text" },
    {
      role: "user",
      content:
        "The quick brown fox jumps over the lazy dog with piercing blue eyes",
    },
  ],
  response_format: zodResponseFormat(EntitiesSchema, "entities"),
})
.on("refusal.done", () => console.log("request refused"))
.on("content.delta", ({ snapshot, parsed }) => {
  console.log("content:", snapshot);
  console.log("parsed:", parsed);
  console.log();
})
.on("content.done", (props) => {
  console.log(props);
});

await stream.done();

const finalCompletion = await stream.finalChatCompletion();

console.log(finalCompletion);
```

You can also use the `stream` helper to parse function call arguments:

```python
from pydantic import BaseModel
import openai
from openai import OpenAI

class GetWeather(BaseModel):
  city: str
  country: str

client = OpenAI()

with client.beta.chat.completions.stream(
  model="gpt-4o",
  messages=[
      {
          "role": "user",
          "content": "What's the weather like in SF and London?",
      },
  ],
  tools=[
      openai.pydantic_function_tool(GetWeather, name="get_weather"),
  ],
  parallel_tool_calls=True,
) as stream:
  for event in stream:
      if event.type == "tool_calls.function.arguments.delta" or event.type == "tool_calls.function.arguments.done":
          print(event)

print(stream.get_final_completion())
```

```js
import { zodFunction } from "openai/helpers/zod";
import OpenAI from "openai/index";
import { z } from "zod";

const GetWeatherArgs = z.object({
city: z.string(),
country: z.string(),
});

const client = new OpenAI();

const stream = client.beta.chat.completions
.stream({
  model: "gpt-4o",
  messages: [
    {
      role: "user",
      content: "What's the weather like in SF and London?",
    },
  ],
  tools: [zodFunction({ name: "get_weather", parameters: GetWeatherArgs })],
})
.on("tool_calls.function.arguments.delta", (props) =>
  console.log("tool_calls.function.arguments.delta", props)
)
.on("tool_calls.function.arguments.done", (props) =>
  console.log("tool_calls.function.arguments.done", props)
)
.on("refusal.delta", ({ delta }) => {
  process.stdout.write(delta);
})
.on("refusal.done", () => console.log("request refused"));

const completion = await stream.finalChatCompletion();

console.log("final completion:", completion);
```

Supported schemas
-----------------

Structured Outputs supports a subset of the [JSON Schema](https://json-schema.org/docs) language.

#### Supported types

The following types are supported for Structured Outputs:

*   String
*   Number
*   Boolean
*   Integer
*   Object
*   Array
*   Enum
*   anyOf

#### Root objects must not be `anyOf`

Note that the root level object of a schema must be an object, and not use `anyOf`. A pattern that appears in Zod (as one example) is using a discriminated union, which produces an `anyOf` at the top level. So code such as the following won't work:

```javascript
import { z } from 'zod';
import { zodResponseFormat } from 'openai/helpers/zod';

const BaseResponseSchema = z.object({ /* ... */ });
const UnsuccessfulResponseSchema = z.object({ /* ... */ });

const finalSchema = z.discriminatedUnion('status', [
  BaseResponseSchema,
  UnsuccessfulResponseSchema,
]);

// Invalid JSON Schema for Structured Outputs
const json = zodResponseFormat(finalSchema, 'final_schema');
```

#### All fields must be `required`

To use Structured Outputs, all fields or function parameters must be specified as `required`.

```json
{
  "name": "get_weather",
  "description": "Fetches the weather in the given location",
  "strict": true,
  "parameters": {
      "type": "object",
      "properties": {
          "location": {
              "type": "string",
              "description": "The location to get the weather for"
          },
          "unit": {
              "type": "string",
              "description": "The unit to return the temperature in",
              "enum": ["F", "C"]
          }
      },
      "additionalProperties": false,
      "required": ["location", "unit"]
  }
}
```

Although all fields must be required (and the model will return a value for each parameter), it is possible to emulate an optional parameter by using a union type with `null`.

```json
{
  "name": "get_weather",
  "description": "Fetches the weather in the given location",
  "strict": true,
  "parameters": {
      "type": "object",
      "properties": {
          "location": {
              "type": "string",
              "description": "The location to get the weather for"
          },
          "unit": {
              "type": ["string", "null"],
              "description": "The unit to return the temperature in",
              "enum": ["F", "C"]
          }
      },
      "additionalProperties": false,
      "required": [
          "location", "unit"
      ]
  }
}
```

#### Objects have limitations on nesting depth and size

A schema may have up to 100 object properties total, with up to 5 levels of nesting.

#### Limitations on total string size

In a schema, total string length of all property names, definition names, enum values, and const values cannot exceed 15,000 characters.

#### Limitations on enum size

A schema may have up to 500 enum values across all enum properties.

For a single enum property with string values, the total string length of all enum values cannot exceed 7,500 characters when there are more than 250 enum values.

#### `additionalProperties: false` must always be set in objects

`additionalProperties` controls whether it is allowable for an object to contain additional keys / values that were not defined in the JSON Schema.

Structured Outputs only supports generating specified keys / values, so we require developers to set `additionalProperties: false` to opt into Structured Outputs.

```json
{
  "name": "get_weather",
  "description": "Fetches the weather in the given location",
  "strict": true,
  "schema": {
      "type": "object",
      "properties": {
          "location": {
              "type": "string",
              "description": "The location to get the weather for"
          },
          "unit": {
              "type": "string",
              "description": "The unit to return the temperature in",
              "enum": ["F", "C"]
          }
      },
      "additionalProperties": false,
      "required": [
          "location", "unit"
      ]
  }
}
```

#### Key ordering

When using Structured Outputs, outputs will be produced in the same order as the ordering of keys in the schema.

#### Some type-specific keywords are not yet supported

Notable keywords not supported include:

*   **For strings:** `minLength`, `maxLength`, `pattern`, `format`
*   **For numbers:** `minimum`, `maximum`, `multipleOf`
*   **For objects:** `patternProperties`, `unevaluatedProperties`, `propertyNames`, `minProperties`, `maxProperties`
*   **For arrays:** `unevaluatedItems`, `contains`, `minContains`, `maxContains`, `minItems`, `maxItems`, `uniqueItems`

If you turn on Structured Outputs by supplying `strict: true` and call the API with an unsupported JSON Schema, you will receive an error.

#### For `anyOf`, the nested schemas must each be a valid JSON Schema per this subset

Here's an example supported anyOf schema:

```json
{
  "type": "object",
  "properties": {
      "item": {
          "anyOf": [
              {
                  "type": "object",
                  "description": "The user object to insert into the database",
                  "properties": {
                      "name": {
                          "type": "string",
                          "description": "The name of the user"
                      },
                      "age": {
                          "type": "number",
                          "description": "The age of the user"
                      }
                  },
                  "additionalProperties": false,
                  "required": [
                      "name",
                      "age"
                  ]
              },
              {
                  "type": "object",
                  "description": "The address object to insert into the database",
                  "properties": {
                      "number": {
                          "type": "string",
                          "description": "The number of the address. Eg. for 123 main st, this would be 123"
                      },
                      "street": {
                          "type": "string",
                          "description": "The street name. Eg. for 123 main st, this would be main st"
                      },
                      "city": {
                          "type": "string",
                          "description": "The city of the address"
                      }
                  },
                  "additionalProperties": false,
                  "required": [
                      "number",
                      "street",
                      "city"
                  ]
              }
          ]
      }
  },
  "additionalProperties": false,
  "required": [
      "item"
  ]
}
```

#### Definitions are supported

You can use definitions to define subschemas which are referenced throughout your schema. The following is a simple example.

```json
{
  "type": "object",
  "properties": {
      "steps": {
          "type": "array",
          "items": {
              "$ref": "#/$defs/step"
          }
      },
      "final_answer": {
          "type": "string"
      }
  },
  "$defs": {
      "step": {
          "type": "object",
          "properties": {
              "explanation": {
                  "type": "string"
              },
              "output": {
                  "type": "string"
              }
          },
          "required": [
              "explanation",
              "output"
          ],
          "additionalProperties": false
      }
  },
  "required": [
      "steps",
      "final_answer"
  ],
  "additionalProperties": false
}
```

#### Recursive schemas are supported

Sample recursive schema using `#` to indicate root recursion.

```json
{
  "name": "ui",
  "description": "Dynamically generated UI",
  "strict": true,
  "schema": {
      "type": "object",
      "properties": {
          "type": {
              "type": "string",
              "description": "The type of the UI component",
              "enum": ["div", "button", "header", "section", "field", "form"]
          },
          "label": {
              "type": "string",
              "description": "The label of the UI component, used for buttons or form fields"
          },
          "children": {
              "type": "array",
              "description": "Nested UI components",
              "items": {
                  "$ref": "#"
              }
          },
          "attributes": {
              "type": "array",
              "description": "Arbitrary attributes for the UI component, suitable for any element",
              "items": {
                  "type": "object",
                  "properties": {
                      "name": {
                          "type": "string",
                          "description": "The name of the attribute, for example onClick or className"
                      },
                      "value": {
                          "type": "string",
                          "description": "The value of the attribute"
                      }
                  },
                  "additionalProperties": false,
                  "required": ["name", "value"]
              }
          }
      },
      "required": ["type", "label", "children", "attributes"],
      "additionalProperties": false
  }
}
```

Sample recursive schema using explicit recursion:

```json
{
  "type": "object",
  "properties": {
      "linked_list": {
          "$ref": "#/$defs/linked_list_node"
      }
  },
  "$defs": {
      "linked_list_node": {
          "type": "object",
          "properties": {
              "value": {
                  "type": "number"
              },
              "next": {
                  "anyOf": [
                      {
                          "$ref": "#/$defs/linked_list_node"
                      },
                      {
                          "type": "null"
                      }
                  ]
              }
          },
          "additionalProperties": false,
          "required": [
              "next",
              "value"
          ]
      }
  },
  "additionalProperties": false,
  "required": [
      "linked_list"
  ]
}
```

JSON mode
---------

JSON mode is a more basic version of the Structured Outputs feature. While JSON mode ensures that model output is valid JSON, Structured Outputs reliably matches the model's output to the schema you specify. We recommend you use Structured Outputs if it is supported for your use case.

When JSON mode is turned on, the model's output is ensured to be valid JSON, except for in some edge cases that you should detect and handle appropriately.

To turn on JSON mode with the Chat Completions or Assistants API you can set the `response_format` to `{ "type": "json_object" }`. If you are using function calling, JSON mode is always turned on.

Important notes:

*   When using JSON mode, you must always instruct the model to produce JSON via some message in the conversation, for example via your system message. If you don't include an explicit instruction to generate JSON, the model may generate an unending stream of whitespace and the request may run continually until it reaches the token limit. To help ensure you don't forget, the API will throw an error if the string "JSON" does not appear somewhere in the context.
*   JSON mode will not guarantee the output matches any specific schema, only that it is valid and parses without errors. You should use Structured Outputs to ensure it matches your schema, or if that is not possible, you should use a validation library and potentially retries to ensure that the output matches your desired schema.
*   Your application must detect and handle the edge cases that can result in the model output not being a complete JSON object (see below)

Handling edge cases

```javascript
const we_did_not_specify_stop_tokens = true;

try {
  const response = await openai.chat.completions.create({
    model: "gpt-3.5-turbo-0125",
    messages: [
      {
        role: "system",
        content: "You are a helpful assistant designed to output JSON.",
      },
      { role: "user", content: "Who won the world series in 2020? Please respond in the format {winner: ...}" },
    ],
    response_format: { type: "json_object" },
  });

  // Check if the conversation was too long for the context window, resulting in incomplete JSON 
  if (response.choices[0].message.finish_reason === "length") {
    // your code should handle this error case
  }

  // Check if the OpenAI safety system refused the request and generated a refusal instead
  if (response.choices[0].message[0].refusal) {
    // your code should handle this error case
    // In this case, the .content field will contain the explanation (if any) that the model generated for why it is refusing
    console.log(response.choices[0].message[0].refusal)
  }

  // Check if the model's output included restricted content, so the generation of JSON was halted and may be partial
  if (response.choices[0].message.finish_reason === "content_filter") {
    // your code should handle this error case
  }

  if (response.choices[0].message.finish_reason === "stop") {
    // In this case the model has either successfully finished generating the JSON object according to your schema, or the model generated one of the tokens you provided as a "stop token"

    if (we_did_not_specify_stop_tokens) {
      // If you didn't specify any stop tokens, then the generation is complete and the content key will contain the serialized JSON object
      // This will parse successfully and should now contain  {"winner": "Los Angeles Dodgers"}
      console.log(JSON.parse(response.choices[0].message.content))
    } else {
      // Check if the response.choices[0].message.content ends with one of your stop tokens and handle appropriately
    }
  }
} catch (e) {
  // Your code should handle errors here, for example a network error calling the API
  console.error(e)
}
```

```python
we_did_not_specify_stop_tokens = True

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "Who won the world series in 2020? Please respond in the format {winner: ...}"}
        ],
        response_format={"type": "json_object"}
    )

    # Check if the conversation was too long for the context window, resulting in incomplete JSON 
    if response.choices[0].message.finish_reason == "length":
        # your code should handle this error case
        pass

    # Check if the OpenAI safety system refused the request and generated a refusal instead
    if response.choices[0].message[0].get("refusal"):
        # your code should handle this error case
        # In this case, the .content field will contain the explanation (if any) that the model generated for why it is refusing
        print(response.choices[0].message[0]["refusal"])

    # Check if the model's output included restricted content, so the generation of JSON was halted and may be partial
    if response.choices[0].message.finish_reason == "content_filter":
        # your code should handle this error case
        pass

    if response.choices[0].message.finish_reason == "stop":
        # In this case the model has either successfully finished generating the JSON object according to your schema, or the model generated one of the tokens you provided as a "stop token"

        if we_did_not_specify_stop_tokens:
            # If you didn't specify any stop tokens, then the generation is complete and the content key will contain the serialized JSON object
            # This will parse successfully and should now contain  "{"winner": "Los Angeles Dodgers"}"
            print(response.choices[0].message.content)
        else:
            # Check if the response.choices[0].message.content ends with one of your stop tokens and handle appropriately
            pass
except Exception as e:
    # Your code should handle errors here, for example a network error calling the API
    print(e)
```

Resources
---------

To learn more about Structured Outputs, we recommend browsing the following resources:

*   Check out our [introductory cookbook](https://cookbook.openai.com/examples/structured_outputs_intro) on Structured Outputs
*   Learn [how to build multi-agent systems](https://cookbook.openai.com/examples/structured_outputs_multi_agent) with Structured Outputs
Function calling
================

Connect models to external data and systems.

**Function calling** enables developers to connect language models to external data and systems. You can define a set of functions as tools that the model has access to, and it can use them when appropriate based on the conversation history. You can then execute those functions on the application side, and provide results back to the model.

Learn how to extend the capabilities of OpenAI models through function calling in this guide.

Experiment with function calling in the [Playground](/playground) by providing your own function definition or generate a ready-to-use definition.

Generate

Overview
--------

Many applications require models to call custom functions to trigger actions within the application or interact with external systems.

Here is how you can define a function as a tool for the model to use:

```python
from openai import OpenAI

client = OpenAI()

tools = [
  {
      "type": "function",
      "function": {
          "name": "get_weather",
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {"type": "string"}
              },
          },
      },
  }
]

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[{"role": "user", "content": "What's the weather like in Paris today?"}],
  tools=tools,
)

print(completion.choices[0].message.tool_calls)
```

```javascript
import { OpenAI } from "openai";
const openai = new OpenAI();

const tools = [
  {
      type: "function",
      function: {
          name: "get_weather",
          parameters: {
              type: "object",
              properties: {
                  location: { type: "string" }
              },
          },
      },
  }
];

const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [{"role": "user", "content": "What's the weather like in Paris today?"}],
  tools,
});

console.log(response.choices[0].message.tool_calls);
```

This will return a function call that looks like this:

```json
[
  {
    "id": "call_12345xyz",
    "type": "function",
    "function": { "name": "get_weather", "arguments": "{'location':'Paris'}" }
  }
]
```

Functions are the only type of tools supported in the Chat Completions API, but the Assistants API also supports [built-in tools](/docs/assistants/tools).

Here are a few examples where function calling can be useful:

1.  **Fetching data:** enable a conversational assistant to retrieve data from internal systems before responding to the user.
2.  **Taking action:** allow an assistant to trigger actions based on the conversation, like scheduling meetings or initiating order returns.
3.  **Building rich workflows:** allow assistants to execute multi-step workflows, like data extraction pipelines or content personalization.
4.  **Interacting with Application UIs:** use function calls to update the user interface based on user input, like rendering a pin on a map or navigating a website.

You can find example use cases in the [examples](#examples) section below.

### The lifecycle of a function call

When you use the OpenAI API with function calling, the model never actually executes functions itself - instead, it simply generates parameters that can be used to call your function. You are then responsible for handling how the function is executed in your code.

Read our [integration guide](#integration-guide) below for more details on how to handle function calls.

![Function Calling diagram](https://cdn.openai.com/API/docs/images/function-calling-diagram.png)

### Function calling support

Function calling is supported in the [Chat Completions API](/docs/guides/text-generation), [Assistants API](/docs/assistants/overview), [Batch API](/docs/guides/batch) and [Realtime API](/docs/guides/realtime).

This guide focuses on function calling using the Chat Completions API. We have separate guides for [function calling using the Assistants API](/docs/assistants/tools/function-calling), and for [function calling using the Realtime API](/docs/guides/realtime#tool-calling).

#### Models supporting function calling

Function calling was introduced with the release of `gpt-4-turbo` on June 13, 2023. All `gpt-*` models released after this date support function calling.

Legacy models released before this date were not trained to support function calling.

Support for parallel function calling

Parallel function calling is supported on models released on or after Nov 6, 2023. This includes: `gpt-4o`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4o-mini`, `gpt-4o-mini-2024-07-18`, `gpt-4-turbo`, `gpt-4-turbo-2024-04-09`, `gpt-4-turbo-preview`, `gpt-4-0125-preview`, `gpt-4-1106-preview`, `gpt-3.5-turbo`, `gpt-3.5-turbo-0125`, and `gpt-3.5-turbo-1106`.

You can find a complete list of models and their release date on our [models page](/docs/models).

Integration guide
-----------------

In this integration guide, we will walk through integrating function calling into an application, taking an order delivery assistant as an example. Rather than requiring users to interact with a form, we can let them ask the assistant for help in natural language.

We will cover how to define functions and instructions, then how to handle model responses and function execution results.

If you want to learn more about how to handle function calls in a streaming fashion, how to customize tool calling behavior or how to handle edge cases, refer to our [advanced usage](#advanced-usage) section.

### Function definition

The starting point for function calling is choosing a function in your own codebase that you'd like to enable the model to generate arguments for.

For this example, let's imagine you want to allow the model to call the `get_delivery_date` function in your codebase which accepts an `order_id` and queries your database to determine the delivery date for a given package. Your function might look something like the following:

```python
# This is the function that we want the model to be able to call
def get_delivery_date(order_id: str) -> datetime:
  # Connect to the database
  conn = sqlite3.connect('ecommerce.db')
  cursor = conn.cursor()
  # ...
```

```javascript
// This is the function that we want the model to be able to call
const getDeliveryDate = async (orderId: string): datetime => { 
  const connection = await createConnection({
      host: 'localhost',
      user: 'root',
      // ...
  });
}
```

Now that we know which function we wish to allow the model to call, we will create a “function definition” that describes the function to the model. This definition describes both what the function does (and potentially when it should be called) and what parameters are required to call the function.

The `parameters` section of your function definition should be described using JSON Schema. If and when the model generates a function call, it will use this information to generate arguments according to your provided schema.

If you want to ensure the model always adheres to your supplied schema, you can enable [Structured Outputs](#structured-outputs) with function calling.

In this example it may look like this:

```json
{
    "name": "get_delivery_date",
    "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
    "parameters": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "string",
                "description": "The customer's order ID."
            }
        },
        "required": ["order_id"],
        "additionalProperties": false
    }
}
```

Next we need to provide our function definitions within an array of available “tools” when calling the Chat Completions API.

As always, we will provide an array of “messages”, which could for example contain your prompt or a back and forth conversation between the user and an assistant.

This example shows how you may call the Chat Completions API providing relevant tools and messages for an assistant that handles customer inquiries for a store.

```python
tools = [
  {
      "type": "function",
      "function": {
          "name": "get_delivery_date",
          "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
          "parameters": {
              "type": "object",
              "properties": {
                  "order_id": {
                      "type": "string",
                      "description": "The customer's order ID.",
                  },
              },
              "required": ["order_id"],
              "additionalProperties": False,
          },
      }
  }
]

messages = [
  {
      "role": "system",
      "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."
  },
  {
      "role": "user",
      "content": "Hi, can you tell me the delivery date for my order?"
  }
]

response = openai.chat.completions.create(
  model="gpt-4o",
  messages=messages,
  tools=tools,
)
```

```javascript
const tools = [
  {
      type: "function",
      function: {
          name: "get_delivery_date",
          description: "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
          parameters: {
              type: "object",
              properties: {
                  order_id: {
                      type: "string",
                      description: "The customer's order ID.",
                  },
              },
              required: ["order_id"],
              additionalProperties: false,
          },
      },
  },
];

const messages = [
  {
      role: "system",
      content: "You are a helpful customer support assistant. Use the supplied tools to assist the user."
  },
  {
      role: "user",
      content: "Hi, can you tell me the delivery date for my order?"
  }
];

const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages,
  tools,
});
```

### Model instructions

While you should define in the function definitions how to call them, we recommend including instructions regarding when to call functions in the system prompt.

For example, you can tell the model when to use the function by saying something like: `"Use the 'get_delivery_date' function when the user asks about their delivery date."`

### Handling model responses

The model only suggests function calls and generates arguments for the defined functions when appropriate. It is then up to you to decide how your application handles the execution of the functions based on these suggestions.

If the model determines that a function should be called, it will return a `tool_calls` field in the response, which you can use to determine if the model generated a function call and what the arguments were.

Unless you customize the tool calling behavior, the model will determine when to call functions based on the instructions and conversation.

Read the [Tool calling behavior](#tool-calling-behavior) section below for more details on how you can force the model to call one or several tools.

#### If the model decides that no function should be called

If the model does not generate a function call, then the response will contain a direct reply to the user as a regular chat completion response.

For example, in this case `chat_response.choices[0].message` may contain:

```python
chat.completionsMessage(
  content='Hi there! I can help with that. Can you please provide your order ID?',
  role='assistant', 
  function_call=None, 
  tool_calls=None
)
```

```javascript
{
  role: 'assistant',
  content: "I'd be happy to help with that. Could you please provide me with your order ID?",
}
```

In an assistant use case you will typically want to show this response to the user and let them respond to it, in which case you will call the API again (with both the latest responses from the assistant and user appended to the `messages`).

Let's assume our user responded with their order id, and we sent the following request to the API.

```python
tools = [
  {
      "type": "function",
      "function": {
          "name": "get_delivery_date",
          "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
          "parameters": {
              "type": "object",
              "properties": {
                  "order_id": {
                      "type": "string",
                      "description": "The customer's order ID."
                  }
              },
              "required": ["order_id"],
              "additionalProperties": False
          }
      }
  }
]

messages = []
messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order?"})
messages.append({"role": "assistant", "content": "Hi there! I can help with that. Can you please provide your order ID?"})
messages.append({"role": "user", "content": "i think it is order_12345"})

response = client.chat.completions.create(
  model='gpt-4o',
  messages=messages,
  tools=tools
)
```

```javascript
const tools = [
  {
      type: "function",
      function: {
          name: "get_delivery_date",
          description: "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
          parameters: {
              type: "object",
              properties: {
                  order_id: {
                      type: "string",
                      escription: "The customer's order ID."
                  }
              },
              required: ["order_id"],
              additionalProperties: false,
          },
      },
  },
];

const messages = [];
messages.push({ role: "system", content: "You are a helpful customer support assistant. Use the supplied tools to assist the user." });
messages.push({ role: "user", content: "Hi, can you tell me the delivery date for my order?" });
messages.push({ role: "assistant", content: "Hi there! I can help with that. Can you please provide your order ID?" });
messages.push({ role: "user", content: "i think it is order_12345" });

const response = await client.chat.completions.create({
  model: 'gpt-4o',
  messages,
  tools,
});
```

#### If the model generated a function call

If the model generated a function call, it will generate the arguments for the call (based on the `parameters` definition you provided).

Here is an example response showing this:

```python
Choice(
  finish_reason='tool_calls', 
  index=0, 
  logprobs=None, 
  message=chat.completionsMessage(
      content=None, 
      role='assistant', 
      function_call=None, 
      tool_calls=[
          chat.completionsMessageToolCall(
              id='call_62136354', 
              function=Function(
                  arguments='{"order_id":"order_12345"}', 
                  name='get_delivery_date'), 
              type='function')
      ])
)
```

```javascript
{
  finish_reason: 'tool_calls',
  index: 0,
  logprobs: null,
  message: {
      content: null,
      role: 'assistant',
      function_call: null,
      tool_calls: [
          {
              id: 'call_62136354',
              function: {
                  arguments: '{"order_id":"order_12345"}',
                  name: 'get_delivery_date'
              },
              type: 'function'
          }
      ]
  }
}
```

#### Handling the model response indicating that a function should be called

Assuming the response indicates that a function should be called, your code will now handle this:

```python
# Extract the arguments for get_delivery_date
# Note this code assumes we have already determined that the model generated a function call. See below for a more production ready example that shows how to check if the model generated a function call
tool_call = response.choices[0].message.tool_calls[0]
arguments = json.loads(tool_call['function']['arguments'])

order_id = arguments.get('order_id')

# Call the get_delivery_date function with the extracted order_id

delivery_date = get_delivery_date(order_id)
```

```javascript
// Extract the arguments for get_delivery_date
// Note this code assumes we have already determined that the model generated a function call. See below for a more production ready example that shows how to check if the model generated a function call
const toolCall = response.choices[0].message.tool_calls[0];
const arguments = JSON.parse(toolCall.function.arguments);

const order_id = arguments.order_id;

// Call the get_delivery_date function with the extracted order_id
const delivery_date = get_delivery_date(order_id);
```

### Submitting function output

Once the function has been executed in the code, you need to submit the result of the function call back to the model.

This will trigger another model response, taking into account the function call result.

For example, this is how you can commit the result of the function call to a conversation history:

```python
# Simulate the order_id and delivery_date
order_id = "order_12345"
delivery_date = datetime.now()

# Simulate the tool call response

response = {
  "choices": [
      {
          "message": {
              "role": "assistant",
              "tool_calls": [
                  {
                      "id": "call_62136354",
                      "type": "function",
                      "function": {
                          "arguments": "{'order_id': 'order_12345'}",
                          "name": "get_delivery_date"
                      }
                  }
              ]
          }
      }
  ]
}

# Create a message containing the result of the function call

function_call_result_message = {
  "role": "tool",
  "content": json.dumps({
      "order_id": order_id,
      "delivery_date": delivery_date.strftime('%Y-%m-%d %H:%M:%S')
  }),
  "tool_call_id": response['choices'][0]['message']['tool_calls'][0]['id']
}

# Prepare the chat completion call payload

completion_payload = {
  "model": "gpt-4o",
  "messages": [
      {"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."},
      {"role": "user", "content": "Hi, can you tell me the delivery date for my order?"},
      {"role": "assistant", "content": "Hi there! I can help with that. Can you please provide your order ID?"},
      {"role": "user", "content": "i think it is order_12345"},
      response['choices'][0]['message'],
      function_call_result_message
  ]
}

# Call the OpenAI API's chat completions endpoint to send the tool call result back to the model

response = openai.chat.completions.create(
  model=completion_payload["model"],
  messages=completion_payload["messages"]
)

# Print the response from the API. In this case it will typically contain a message such as "The delivery date for your order #12345 is xyz. Is there anything else I can help you with?"

print(response)
```

```javascript
// Simulate the order_id and delivery_date
const order_id = "order_12345";
const delivery_date = moment();

// Simulate the tool call response
const response = {
  choices: [
      {
          message: {
              tool_calls: [
                  { id: "tool_call_1" }
              ]
          }
      }
  ]
};

// Create a message containing the result of the function call
const function_call_result_message = {
  role: "tool",
  content: JSON.stringify({
      order_id: order_id,
      delivery_date: delivery_date.format('YYYY-MM-DD HH:mm:ss')
  }),
  tool_call_id: response.choices[0].message.tool_calls[0].id
};

// Prepare the chat completion call payload
const completion_payload = {
  model: "gpt-4o",
  messages: [
      { role: "system", content: "You are a helpful customer support assistant. Use the supplied tools to assist the user." },
      { role: "user", content: "Hi, can you tell me the delivery date for my order?" },
      { role: "assistant", content: "Hi there! I can help with that. Can you please provide your order ID?" },
      { role: "user", content: "i think it is order_12345" },
      response.choices[0].message,
      function_call_result_message
  ]
};

// Call the OpenAI API's chat completions endpoint to send the tool call result back to the model
const final_response = await openai.chat.completions.create({
  model: completion_payload.model,
  messages: completion_payload.messages
});

// Print the response from the API. In this case it will typically contain a message such as "The delivery date for your order #12345 is xyz. Is there anything else I can help you with?"
console.log(final_response);
```

Note that an assistant message containing tool calls should always be followed by tool response messages (one per tool call). Making an API call with a messages array that does not follow this pattern will result in an error.

Structured Outputs
------------------

In August 2024, we launched Structured Outputs, which ensures that a model's output exactly matches a specified JSON schema.

By default, when using function calling, the API will offer best-effort matching for your parameters, which means that occasionally the model may miss parameters or get their types wrong when using complicated schemas.

You can enable Structured Outputs for function calling by setting the parameter `strict: true` in your function definition. You should also include the parameter `additionalProperties: false` and mark all arguments as required in your request. When this is enabled, the function arguments generated by the model will be constrained to match the JSON Schema provided in the function definition.

As an alternative to function calling you can instead constrain the model's regular output to match a JSON Schema of your choosing. [Learn more](/docs/guides/structured-outputs#function-calling-vs-response-format) about when to use function calling vs when to control the model's normal output by using `response_format`.

### Parallel function calling and Structured Outputs

When the model outputs multiple function calls via parallel function calling, model outputs may not match strict schemas supplied in tools.

In order to ensure strict schema adherence, disable parallel function calls by supplying `parallel_tool_calls: false`. With this setting, the model will generate one function call at a time.

### Why might I not want to turn on Structured Outputs?

The main reasons to not use Structured Outputs are:

*   If you need to use some feature of JSON Schema that is not yet supported ([learn more](/docs/guides/structured-outputs#supported-schemas)), for example recursive schemas.
*   If each of your API requests includes a novel schema (i.e. your schemas are not fixed, but are generated on-demand and rarely repeat). The first request with a novel JSON schema will have increased latency as the schema is pre-processed and cached for future generations to constrain the output of the model.

### What does Structured Outputs mean for Zero Data Retention?

When Structured Outputs is turned on, schemas provided are not eligible for [zero data retention](/docs/models#how-we-use-your-data).

### Supported schemas

Function calling with Structured Outputs supports a subset of the JSON Schema language.

For more information on supported schemas, see the [Structured Outputs guide](/docs/guides/structured-outputs#supported-schemas).

### Example

You can use zod in nodeJS and Pydantic in python when using the SDKs to pass your function definitions to the model.

```javascript
import OpenAI from "openai";
import { z } from "zod";
import { zodFunction } from "openai/helpers/zod";

const OrderParameters = z.object({
  order_id: z.string().describe("The customer's order ID."),
});

const tools = [
  zodFunction({ name: "getDeliveryDate", parameters: OrderParameters }),
];

const messages = [
  {
    role: "system",
    content: "You are a helpful customer support assistant. Use the supplied tools to assist the user.",
  },
  {
    role: "user",
    content: "Hi, can you tell me the delivery date for my order #12345?",
  },
];

const openai = new OpenAI();

const response = await openai.beta.chat.completions.create({
  model: "gpt-4o-2024-08-06",
  messages,
  tools,
});

console.log(response.choices[0].message.tool_calls?.[0].function);
```

```python
from enum import Enum
from typing import Union
from pydantic import BaseModel
import openai
from openai import OpenAI

client = OpenAI()

class GetDeliveryDate(BaseModel):
    order_id: str

tools = [openai.pydantic_function_tool(GetDeliveryDate)]

messages = []
messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order #12345?"})

response = client.beta.chat.completions.create(
    model='gpt-4o-2024-08-06',
    messages=messages,
    tools=tools
)

print(response.choices[0].message.tool_calls[0].function)
```

```bash
curl https://api.openai.com/v1/chat/completions \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."
            },
            {
                "role": "user",
                "content": "Hi, can you tell me the delivery date for my order #12345?"
            }
        ],
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "get_delivery_date",
                    "description": "Get the delivery date for a customer’s order. Call this whenever you need to know the delivery date, for example when a customer asks \"Where is my package\"",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "order_id": {
                                "type": "string",
                                "description": "The customer’s order ID."
                            }
                        },
                        "required": ["order_id"],
                        "additionalProperties": false
                    }
                },
                "strict": true
            }
        ]
    }'
```

If you are not using the SDKs, add the `strict: true` parameter to your function definition. Additionally, all parameters must be included in the `required` array, and `additionalProperties: false` must be set.

```json
{
    "name": "get_delivery_date",
    "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks \\"Where is my package\\"",
    "strict": true,
    "parameters": {
        "type": "object",
        "properties": {
            "order_id": { "type": "string" }
        },
        "required": ["order_id"],
        "additionalProperties": false,
    }
}
```

### Limitations

When you use Structured Outputs with function calling, the model will always follow your exact schema, except in a few circumstances:

*   When the model's response is cut off (either due to `max_tokens`, `stop_tokens`, or maximum context length)
*   When a model [refusal](/docs/guides/structured-outputs#refusals) happens
*   When there is a `content_filter` finish reason

Note that the first time you send a request with a new schema using Structured Outputs, there will be additional latency as the schema is processed, but subsequent requests should incur no overhead.

Advanced usage
--------------

### Streaming tool calls

You can stream tool calls and process function arguments as they are being generated. This is especially useful if you want to display the function arguments in your UI, or if you don't need to wait for the whole function parameters to be generated before executing the function.

To enable streaming tool calls, you can set `stream: true` in your request. You can then process the streaming delta and check for any new tool calls delta.

You can find more information on streaming in the [API reference](/docs/api-reference/streaming).

Here is an example of how you can handle streaming tool calls with the node and python SDKs:

```python
from openai import OpenAI
import json

client = OpenAI()

# Define functions
tools = [
  {
      "type": "function",
      "function": {
          "name": "generate_recipe",
          "description": "Generate a recipe based on the user's input",
          "parameters": {
              "type": "object",
              "properties": {
                  "title": {
                      "type": "string",
                      "description": "Title of the recipe.",
                  },
                  "ingredients": {
                      "type": "array",
                      "items": {"type": "string"},
                      "description": "List of ingredients required for the recipe.",
                  },
                  "instructions": {
                      "type": "array",
                      "items": {"type": "string"},
                      "description": "Step-by-step instructions for the recipe.",
                  },
              },
              "required": ["title", "ingredients", "instructions"],
              "additionalProperties": False,
          },
      },
  }
]

response_stream = client.chat.completions.create(
  model="gpt-4o",
  messages=[
      {
          "role": "system",
          "content": (
              "You are an expert cook who can help turn any user input into a delicious recipe."
              "As soon as the user tells you what they want, use the generate_recipe tool to create a detailed recipe for them."
          ),
      },
      {
          "role": "user",
          "content": "I want to make pancakes for 4.",
      },
  ],
  tools=tools,
  stream=True,
)

function_arguments = ""
function_name = ""
is_collecting_function_args = False

for part in response_stream:
  delta = part.choices[0].delta
  finish_reason = part.choices[0].finish_reason

  # Process assistant content
  if 'content' in delta:
      print("Assistant:", delta.content)

  if delta.tool_calls:
      is_collecting_function_args = True
      tool_call = delta.tool_calls[0]

      if tool_call.function.name:
          function_name = tool_call.function.name
          print(f"Function name: '{function_name}'")
      
      # Process function arguments delta
      if tool_call.function.arguments:
          function_arguments += tool_call.function.arguments
          print(f"Arguments: {function_arguments}")

  # Process tool call with complete arguments
  if finish_reason == "tool_calls" and is_collecting_function_args:
      print(f"Function call '{function_name}' is complete.")
      args = json.loads(function_arguments)
      print("Complete function arguments:")
      print(json.dumps(args, indent=2))
   
      # Reset for the next potential function call
      function_arguments = ""
      function_name = ""
      is_collecting_function_args = False
```

```javascript
import OpenAI from "openai";

const openai = new OpenAI();

// Define functions
const tools = [
{
  type: "function",
  function: {
    name: "generate_recipe",
    description: "Generate a recipe based on the user's input",
    parameters: {
      type: "object",
      properties: {
        title: {
          type: "string",
          description: "Title of the recipe.",
        },
        ingredients: {
          type: "array",
          items: { type: "string" },
          description: "List of ingredients required for the recipe.",
        },
        instructions: {
          type: "array",
          items: { type: "string" },
          description: "Step-by-step instructions for the recipe.",
        },
      },
      required: ["title", "ingredients", "instructions"],
      additionalProperties: false,
    },
  },
},
];

const responseStream = await openai.chat.completions.create({
model: "gpt-4o",
messages: [
  {
    role: "system",
    content:
      "You are an expert cook who can help turn any user input into a delicious recipe. As soon as the user tells you what they want, use the generate_recipe tool to create a detailed recipe for them.",
  },
  {
    role: "user",
    content: "I want to make pancakes for 4.",
  },
],
tools: tools,
stream: true,
});

let functionArguments = "";
let functionName = "";
let isCollectingFunctionArgs = false;

for await (const part of responseStream) {
const delta = part.choices[0].delta;
const finishReason = part.choices[0].finish_reason;

if (delta.content) {
  // Process assistant content
  console.log("Assistant:", delta.content);
}

if (delta.tool_calls) {
  isCollectingFunctionArgs = true;
  const toolCall = delta.tool_calls[0];

  if (toolCall.function?.name) {
    functionName = toolCall.function.name;
    console.log("Function name:", functionName);
  }

  if (toolCall.function?.arguments) {
    functionArguments += toolCall.function.arguments;
    // Process function arguments delta
    console.log(`Arguments: ${functionArguments}`);
  }
}

// Process tool call with complete arguments
if (finishReason === "tool_calls" && isCollectingFunctionArgs) {
  console.log(`Function call '${functionName}' is complete.`);

  const args = JSON.parse(functionArguments);
  console.log("Complete function arguments:", args);

  // Reset for the next potential function call
  functionArguments = "";
  functionName = "";
  isCollectingFunctionArgs = false;
}
}
```

### Tool calling behavior

The API supports advanced features such as parallel tool calling and the ability to force tool calls.

You can disable parallel tool calling by setting `parallel_tool_calls: false`.

Parallel tool calling

Any models released on or after Nov 6, 2023 may by default generate multiple tool calls in a single response, indicating that they should be called in parallel.

This is especially useful if executing the given functions takes a long time. For example, the model may call functions to get the weather in 3 different locations at the same time, which will result in a message with 3 function calls in the tool\_calls array.

Example response:

```python
response = Choice(
  finish_reason='tool_calls', 
  index=0, 
  logprobs=None, 
  message=chat.completionsMessage(
      content=None, 
      role='assistant', 
      function_call=None, 
      tool_calls=[
          chat.completionsMessageToolCall(
              id='call_62136355', 
              function=Function(
                  arguments='{"city":"New York"}', 
                  name='check_weather'), 
              type='function'),
          chat.completionsMessageToolCall(
              id='call_62136356', 
              function=Function(
                  arguments='{"city":"London"}', 
                  name='check_weather'), 
              type='function'),
          chat.completionsMessageToolCall(
              id='call_62136357', 
              function=Function(
                  arguments='{"city":"Tokyo"}', 
                  name='check_weather'), 
              type='function')
      ])
)

# Iterate through tool calls to handle each weather check

for tool_call in response.message.tool_calls:
  arguments = json.loads(tool_call.function.arguments)
  city = arguments['city']
  weather_info = check_weather(city)
  print(f"Weather in {city}: {weather_info}")
```

```javascript
const response = {
  finish_reason: 'tool_calls',
  index: 0,
  logprobs: null,
  message: {
      content: null,
      role: 'assistant',
      function_call: null,
      tool_calls: [
          {
              id: 'call_62136355',
              function: {
                  arguments: '{"city":"New York"}',
                  name: 'check_weather'
              },
              type: 'function'
          },
          {
              id: 'call_62136356',
              function: {
                  arguments: '{"city":"London"}',
                  name: 'check_weather'
              },
              type: 'function'
          },
          {
              id: 'call_62136357',
              function: {
                  arguments: '{"city":"Tokyo"}',
                  name: 'check_weather'
              },
              type: 'function'
          }
      ]
  }
};

// Iterate through tool calls to handle each weather check
response.message.tool_calls.forEach(tool_call => {
  const arguments = JSON.parse(tool_call.function.arguments);
  const city = arguments.city;
  check_weather(city).then(weather_info => {
      console.log(`Weather in ${city}: ${weather_info}`);
  });
});
```

Each function call in the array has a unique `id`.

Once you've executed these function calls in your application, you can provide the result back to the model by adding one new message to the conversation for each function call, each containing the result of one function call, with a `tool_call_id` referencing the `id` from `tool_calls`, for example:

```python
# Assume we have fetched the weather data from somewhere
weather_data = {
  "New York": {"temperature": "22°C", "condition": "Sunny"},
  "London": {"temperature": "15°C", "condition": "Cloudy"},
  "Tokyo": {"temperature": "25°C", "condition": "Rainy"}
}
  
# Prepare the chat completion call payload with inline function call result creation
completion_payload = {
  "model": "gpt-4o",
  "messages": [
      {"role": "system", "content": "You are a helpful assistant providing weather updates."},
      {"role": "user", "content": "Can you tell me the weather in New York, London, and Tokyo?"},
      # Append the original function calls to the conversation
      response['message'],
      # Include the result of the function calls
      {
          "role": "tool",
          "content": json.dumps({
              "city": "New York",
              "weather": weather_data["New York"]
          }),
          # Here we specify the tool_call_id that this result corresponds to
          "tool_call_id": response['message']['tool_calls'][0]['id']
      },
      {
          "role": "tool",
          "content": json.dumps({
              "city": "London",
              "weather": weather_data["London"]
          }),
          "tool_call_id": response['message']['tool_calls'][1]['id']
      },
      {
          "role": "tool",
          "content": json.dumps({
              "city": "Tokyo",
              "weather": weather_data["Tokyo"]
          }),
          "tool_call_id": response['message']['tool_calls'][2]['id']
      }
  ]
}
  
# Call the OpenAI API's chat completions endpoint to send the tool call result back to the model
response = openai.chat.completions.create(
  model=completion_payload["model"],
  messages=completion_payload["messages"]
)
  
# Print the response from the API, which will return something like "In New York the weather is..."
print(response)
```

```javascript
// Assume we have fetched the weather data from somewhere
const weather_data = {
  "New York": { "temperature": "22°C", "condition": "Sunny" },
  "London": { "temperature": "15°C", "condition": "Cloudy" },
  "Tokyo": { "temperature": "25°C", "condition": "Rainy" }
};

// Prepare the chat completion call payload with inline function call result creation
const completion_payload = {
  model: "gpt-4o",
  messages: [
      { role: "system", content: "You are a helpful assistant providing weather updates." },
      { role: "user", content: "Can you tell me the weather in New York, London, and Tokyo?" },
      // Append the original function calls to the conversation
      response.message,
      // Include the result of the function calls
      {
          role: "tool",
          content: JSON.stringify({
              city: "New York",
              weather: weather_data["New York"]
          }),
          // Here we specify the tool_call_id that this result corresponds to
          tool_call_id: response.message.tool_calls[0].id
      },
      {
          role: "tool",
          content: JSON.stringify({
              city: "London",
              weather: weather_data["London"]
          }),
          tool_call_id: response.message.tool_calls[1].id
      },
      {
          role: "tool",
          content: JSON.stringify({
              city: "Tokyo",
              weather: weather_data["Tokyo"]
          }),
          tool_call_id: response.message.tool_calls[2].id
      }
  ]
};

// Call the OpenAI API's chat completions endpoint to send the tool call result back to the model
const response = await openai.chat.completions.create({
  model: completion_payload.model,
  messages: completion_payload.messages
});

// Print the response from the API, which will return something like "In New York the weather is..."
console.log(response);
```

Forcing tool calls

By default, the model is configured to automatically select which tools to call, as determined by the `tool_choice: "auto"` setting.

We offer three ways to customize the default behavior:

1.  To force the model to always call one or more tools, you can set `tool_choice: "required"`. The model will then always select one or more tool(s) to call. This is useful for example if you want the model to pick between multiple actions to perform next
2.  To force the model to call a specific function, you can set `tool_choice: {"type": "function", "function": {"name": "my_function"}}`
3.  To disable function calling and force the model to only generate a user-facing message, you can either provide no tools, or set `tool_choice: "none"`

Note that if you do either 1 or 2 (i.e. force the model to call a function) then the subsequent `finish_reason` will be `"stop"` instead of being `"tool_calls"`.

```python
from openai import OpenAI

client = OpenAI()

tools = [
  {
      "type": "function",
      "function": {
          "name": "get_weather",
          "strict": True,
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {"type": "string"},
                  "unit": {"type": "string", "enum": ["c", "f"]},
              },
              "required": ["location", "unit"],
              "additionalProperties": False,
          },
      },
  },
  {
      "type": "function",
      "function": {
          "name": "get_stock_price",
          "strict": True,
          "parameters": {
              "type": "object",
              "properties": {
                  "symbol": {"type": "string"},
              },
              "required": ["symbol"],
              "additionalProperties": False,
          },
      },
  },
]

messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=messages,
  tools=tools,
  tool_choice="required"
)

print(completion)
```

```javascript
import { OpenAI } from "openai";
const openai = new OpenAI();

// Define a set of tools to use
const tools = [
  {
      type: "function",
      function: {
          name: "get_weather",
          strict: true,
          parameters: {
              type: "object",
              properties: {
                  location: { type: "string" },
                  unit: { type: "string", enum: ["c", "f"] },
              },
              required: ["location", "unit"],
              additionalProperties: false,
          },
      },
  },
  {
      type: "function",
      function: {
          name: "get_stock_price",
          strict: true,
          parameters: {
              type: "object",
              properties: {
                  symbol: { type: "string" },
              },
              required: ["symbol"],
              additionalProperties: false,
          },
      },
  },
];

// Call the OpenAI API's chat completions endpoint
const response = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
      {
          role: "user",
          content: "Can you tell me the weather in Tokyo?",
      },
  ],
  tool_choice: "required",
  tools,
});

// Print the response from the API
console.log(response);
```

To see a practical example of how to force tool calls, see our cookbook:

[

Customer service with tool required

Learn how to add an element of determinism to your customer service assistant

](https://cookbook.openai.com/examples/using_tool_required_for_customer_service)

### Edge cases

We recommend using the SDK to handle the edge cases described below. If for any reason you cannot use the SDK, you should handle these cases in your code.

When you receive a response from the API, if you're not using the SDK, there are a number of edge cases that production code should handle.

In general, the API will return a valid function call, but there are some edge cases when this won't happen:

*   When you have specified `max_tokens` and the model's response is cut off as a result
*   When the model's output includes copyrighted material

Also, when you force the model to call a function, the `finish_reason` will be `"stop"` instead of `"tool_calls"`.

This is how you can handle these different cases in your code:

```python
# Check if the conversation was too long for the context window
if response['choices'][0]['message']['finish_reason'] == "length":
  print("Error: The conversation was too long for the context window.")
  # Handle the error as needed, e.g., by truncating the conversation or asking for clarification
  handle_length_error(response)
  
# Check if the model's output included copyright material (or similar)
if response['choices'][0]['message']['finish_reason'] == "content_filter":
  print("Error: The content was filtered due to policy violations.")
  # Handle the error as needed, e.g., by modifying the request or notifying the user
  handle_content_filter_error(response)
  
# Check if the model has made a tool_call. This is the case either if the "finish_reason" is "tool_calls" or if the "finish_reason" is "stop" and our API request had forced a function call
if (response['choices'][0]['message']['finish_reason'] == "tool_calls" or 
  # This handles the edge case where if we forced the model to call one of our functions, the finish_reason will actually be "stop" instead of "tool_calls"
  (our_api_request_forced_a_tool_call and response['choices'][0]['message']['finish_reason'] == "stop")):
  # Handle tool call
  print("Model made a tool call.")
  # Your code to handle tool calls
  handle_tool_call(response)
  
# Else finish_reason is "stop", in which case the model was just responding directly to the user
elif response['choices'][0]['message']['finish_reason'] == "stop":
  # Handle the normal stop case
  print("Model responded directly to the user.")
  # Your code to handle normal responses
  handle_normal_response(response)
  
# Catch any other case, this is unexpected
else:
  print("Unexpected finish_reason:", response['choices'][0]['message']['finish_reason'])
  # Handle unexpected cases as needed
  handle_unexpected_case(response)
```

```javascript
// Check if the conversation was too long for the context window
if (response.choices[0].message.finish_reason === "length") {
  console.log("Error: The conversation was too long for the context window.");
  // Handle the error as needed, e.g., by truncating the conversation or asking for clarification
  handleLengthError(response);
}

// Check if the model's output included copyright material (or similar)
if (response.choices[0].message.finish_reason === "content_filter") {
  console.log("Error: The content was filtered due to policy violations.");
  // Handle the error as needed, e.g., by modifying the request or notifying the user
  handleContentFilterError(response);
}

// Check if the model has made a tool_call. This is the case either if the "finish_reason" is "tool_calls" or if the "finish_reason" is "stop" and our API request had forced a function call
if (
  response.choices[0].message.finish_reason === "tool_calls" ||
  (ourApiRequestForcedAToolCall && response.choices[0].message.finish_reason === "stop")
) {
  // Handle tool call
  console.log("Model made a tool call.");
  // Your code to handle tool calls
  handleToolCall(response);
}

// Else finish_reason is "stop", in which case the model was just responding directly to the user
else if (response.choices[0].message.finish_reason === "stop") {
  // Handle the normal stop case
  console.log("Model responded directly to the user.");
  // Your code to handle normal responses
  handleNormalResponse(response);
}

// Catch any other case, this is unexpected
else {
  console.log("Unexpected finish_reason:", response.choices[0].message.finish_reason);
  // Handle unexpected cases as needed
  handleUnexpectedCase(response);
}
```

### Token usage

Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means functions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions or the length of the descriptions you provide for function parameters.

It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined in your tools specification.

Examples
--------

The [OpenAI Cookbook](https://cookbook.openai.com/) has several end-to-end examples to help you implement function calling.

In our introductory cookbook [how to call functions with chat models](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models), we outline two examples of how the models can use function calling. This is a great resource to follow as you get started:

[

Function calling

Learn from more examples demonstrating function calling

](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)

You will also find examples of function definitions for common use cases below.

Shopping Assistant

#### Scenario

A shopping assistant helps users navigate an e-commerce site. It needs to fetch product data from a structured database, and suggest recommendations based on the user's query. Once the user has found a product they are interested in, the assistant can add it to the shopping cart on their behalf.

#### Function definitions

To recommend products to the user, the assistant needs to query the products database. To find more details about a product, such as reviews and additional information (e.g. materials, dimensions...), the assistant needs to fetch more information on the specific product. It also needs a tool to add items to the shopping cart.

We will then define the following functions:

*   `get_product_recommendations`: Recommends products based on filters
*   `get_product_details`: Fetches more details about a product
*   `add_to_cart`: Adds a product to the shopping cart

```json
[
    {
        "type": "function",
        "function": {
            "name": "get_product_recommendations",
            "description": "Searches for products matching certain criteria in the database",
            "parameters": {
                "type": "object",
                "properties": {
                    "categories": {
                        "description": "categories that could be a match",
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "coats & jackets",
                                "accessories",
                                "tops",
                                "jeans & trousers",
                                "skirts & dresses",
                                "shoes"
                            ]
                        }
                    },
                    "colors": {
                        "description": "colors that could be a match, empty array if N/A",
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "black",
                                "white",
                                "brown",
                                "red",
                                "blue",
                                "green",
                                "orange",
                                "yellow",
                                "pink",
                                "gold",
                                "silver"
                            ]
                        }
                    },
                    "keywords": {
                        "description": "keywords that should be present in the item title or description",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "price_range": {
                        "type": "object",
                        "properties": {
                            "min": {
                                "type": "number"
                            },
                            "max": {
                                "type": "number"
                            }
                        },
                        "required": [
                        "min",
                        "max"
                        ],
                        "additionalProperties": false
                    },
                    "limit": {
                        "type": "integer",
                        "description": "The maximum number of products to return, use 5 by default if nothing is specified by the user"
                    }
                },
                "required": [
                    "categories",
                    "colors",
                    "keywords",
                    "price_range",
                    "limit"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_details",
            "description": "Fetches more details about a product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The ID of the product to fetch details for"
                    }
                },
                "required": [
                    "product_id"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_to_cart",
            "description": "Add items to cart when the user has confirmed their interest.",
            "parameters": {
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product_id": {
                                    "type": "string",
                                    "description": "ID of the product to add to the cart"
                                },
                                "quantity": {
                                    "type": "integer",
                                    "description": "Quantity of the product to add to the cart"
                                }
                            },
                            "required": [
                                "product_id",
                                "quantity"
                            ],
                            "additionalProperties": false
                        }
                    },
                    "required": [
                        "items"
                    ],
                    "additionalProperties": false
                }
            }
        }
    }
]
```

Customer Service Agent

#### Scenario

A customer service assistant on an e-commerce site helps users after they have made a purchase. It can answer questions about their orders or the company policy regarding returns and refunds. It can also help customers process a return and give status updates.

#### Function definitions

To answer questions about orders, the assistant needs to fetch order details from the orders database. In case the user doesn't know their order number, the assistant should also be able to fetch the last orders for a given user. It should also be able to search the FAQ to respond to general questions. Lastly, it should be equipped with tools to process returns and find a return status.

We will then define the following functions:

*   `get_order_details`: Fetches details about a specific order
*   `get_user_orders`: Fetches the last orders for a given user
*   `search_faq`: Searches the FAQ for an answer to the user's question
*   `process_return`: Processes a return and creates a return label
*   `get_return_status`: Finds the status of a return

```json
[
    {
        "type": "function",
        "function": {
            "name": "get_order_details",
            "description": "Fetches details about a specific order",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The ID of the order to fetch details for"
                    }
                },
                "required": [
                    "order_id"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_user_orders",
            "description": "Fetches the last orders for a given user",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "description": "The ID of the user to fetch orders for"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "The maximum number of orders to return, use 5 by default and increase the number if the relevant order is not found."
                    }
                },
                "required": [
                    "user_id", "limit"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_faq",
            "description": "Searches the FAQ for an answer to the user's question",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The question to search the FAQ for"
                    }
                },
                "required": [
                    "query"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "process_return",
            "description": "Processes a return and creates a return label",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The ID of the order to process a return for"
                    },
                    "items": {
                        "type": "array",
                        "description": "The items to return",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product_id": {
                                    "type": "string",
                                    "description": "The ID of the product to return"
                                },
                                "quantity": {
                                    "type": "integer",
                                    "description": "The quantity of the product to return"
                                }
                            },
                            "required": [
                                "product_id",
                                "quantity"
                            ],
                            "additionalProperties": false
                        }
                    }
                },
                "required": [
                    "order_id",
                    "items"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_return_status",
            "description": "Finds the status of a return",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The ID of the order to fetch the return status for"
                    }
                },
                "required": [
                    "order_id"
                ],
                "additionalProperties": false
            }
        }
    }
]
```

Interactive Booking Experience

#### Scenario

A user is on an interactive website to find a place to eat or stay. After they mention their preferences, the website updates to show recommendations on a map. Once they have found a place they are interested in, a booking is programmatically made on their behalf.

#### Function definitions

To be able to show recommendations, the app needs to first fetch recommendations based on the user's preferences, and then pin those recommendations on the map. To book a place, the assistant needs to fetch the availability of the place, and then create a booking on the user's behalf.

We will then define the following functions:

*   `get_recommendations`: Fetche recommendations based on the user's preferences
*   `show_on_map`: Place pins on the map
*   `fetch_availability`: Fetch the availability for a given place
*   `create_booking`: Create a booking on the user's behalf

```json
[
    {
        "type": "function",
        "function": {
            "name": "get_recommendations",
            "description": "Fetches recommendations based on the user's preferences",
            "parameters": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "The type of place to search recommendations for",
                        "enum": ["restaurant", "hotel"]
                    },
                    "keywords": {
                        "type": "array",
                        "description": "Keywords that should be present in the recommendations",
                        "items": {
                            "type": "string"
                        }
                    },
                    "location": {
                        "type": "string",
                        "description": "The location to search recommendations for"
                    }
                },
                "required": [
                    "type",
                    "keywords",
                    "location"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "show_on_map",
            "description": "Places pins on the map for relevant locations",
            "parameters": {
                "type": "object",
                "properties": {
                    "pins": {
                        "type": "array",
                        "description": "The pins to place on the map",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "The name of the place"
                                },
                                "coordinates": {
                                    "type": "object",
                                    "properties": {
                                        "latitude": { "type": "number" },
                                        "longitude": { "type": "number" }
                                    },
                                    "required": [
                                        "latitude",
                                        "longitude"
                                    ],
                                    "additionalProperties": false
                                }
                            },
                            "required": [
                                "name",
                                "coordinates"
                            ],
                            "additionalProperties": false
                        }
                    }
                },
                "required": [
                    "pins"
                ],
                "additionalProperties": false
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_availability",
            "description": "Fetches the availability for a given place",
            "parameters": {
                "type": "object",
                "properties": {
                    "place_id": {
                        "type": "string",
                        "description": "The ID of the place to fetch availability for"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_booking",
            "description": "Creates a booking on the user's behalf",
            "parameters": {
                "type": "object",
                "properties": {
                    "place_id": {
                        "type": "string",
                        "description": "The ID of the place to create a booking for"
                    },
                    "booking_details": {
                        "anyOf": [
                            {
                                "type": "object",
                                "description": "Restaurant booking with specific date and time",
                                "properties": {
                                    "date": {
                                        "type": "string",
                                        "description": "The date of the booking, in format YYYY-MM-DD"
                                    },
                                    "time": {
                                        "type": "string",
                                        "description": "The time of the booking, in format HH:MM"
                                    }
                                },
                                "required": [
                                    "date",
                                    "time"
                                ]
                            },
                            {
                                "type": "object",
                                "description": "Hotel booking with specific check-in and check-out dates",
                                "properties": {
                                    "check_in": {
                                        "type": "string",
                                        "description": "The check-in date of the booking, in format YYYY-MM-DD"
                                    },
                                    "check_out": {
                                        "type": "string",
                                        "description": "The check-out date of the booking, in format YYYY-MM-DD"
                                    }
                                },
                                "required": [
                                    "check_in",
                                    "check_out"
                                ]
                            }
                        ]
                    }
                },
                "required": [
                    "place_id",
                    "booking_details"
                ],
                "additionalProperties": false
            }
        }
    }
]
```

Best practices
--------------

### Turn on Structured Outputs by setting `strict: "true"`

When Structured Outputs is turned on, the arguments generated by the model for function calls will reliably match the JSON Schema that you provide.

If you are not using Structured Outputs, then the structure of arguments is not guaranteed to be correct, so we recommend the use of a validation library like Pydantic to first verify the arguments prior to using them.

### Name functions intuitively, with detailed descriptions

If you find the model does not generate calls to the correct functions, you may need to update your function names and descriptions so the model more clearly understands when it should select each function. Avoid using abbreviations or acronyms to shorten function and argument names.

You can also include detailed descriptions for when a function should be called. For complex functions, you should include descriptions for each of the arguments to help the model know what it needs to ask the user to collect that argument.

### Name function parameters intuitively, with detailed descriptions

Use clear and descriptive names for function parameters. If applicable, specify the expected format for a parameter in the description (e.g., YYYY-mm-dd or dd/mm/yy for a date).

### Consider providing additional information about how and when to call functions in your system message

Providing clear instructions in your system message can significantly improve the model's function calling accuracy. For example, guide the model with instructions like the following:

`"Use check_order_status when the user inquires about the status of their order, such as 'Where is my order?' or 'Has my order shipped yet?'".`

Provide context for complex scenarios. For example:

`"Before scheduling a meeting with schedule_meeting, check the user's calendar for availability using check_availability to avoid conflicts."`

### Use enums for function arguments when possible

If your use case allows, you can use enums to constrain the possible values for arguments. This can help reduce hallucinations.

For example, if you have an AI assistant that helps with ordering a T-shirt, you likely have a fixed set of sizes for the T-shirt that you might want to constrain the model to choose from. If you want the model to output “s”, “m”, “l”, for small, medium, and large, you could provide those values in an enum, like this:

```json
{
    "name": "pick_tshirt_size",
    "description": "Call this if the user specifies which size t-shirt they want",
    "parameters": {
        "type": "object",
        "properties": {
            "size": {
                "type": "string",
                "enum": ["s", "m", "l"],
                "description": "The size of the t-shirt that the user would like to order"
            }
        },
        "required": ["size"],
        "additionalProperties": false
    }
}
```

If you don't constrain the output, a user may say “large” or “L”, and the model may use these values as a parameter. As your code may expect a specific structure, it's helpful to limit the possible values the model can choose from.

### Keep the number of functions low for higher accuracy

We recommend that you use no more than 20 tools in a single API call.

Developers typically see a reduction in the model's ability to select the correct tool once they have between 10-20 tools defined.

If your use case requires the model to be able to pick between a large number of custom functions, you may want to explore fine-tuning ([learn more](https://cookbook.openai.com/examples/fine_tuning_for_function_calling)) or break out the tools and group them logically to create a multi-agent system.

### Set up evals to act as an aid in prompt engineering your function definitions and system messages

We recommend for non-trivial uses of function calling setting up an evaluation system that allow you to measure how frequently the correct function is called or correct arguments are generated for a wide variety of possible user messages. Learn more about setting up evals on the [OpenAI Cookbook](https://cookbook.openai.com/examples/evaluation/getting_started_with_openai_evals).

You can then use these to measure whether adjustments to your function definitions and system messages will improve or hurt your integration.

### Fine-tuning may help improve accuracy for function calling

Fine-tuning a model can improve performance at function calling for your use case, especially if you have a large number of functions, or complex, nuanced or similar functions.

See our fine-tuning for function calling [cookbook](https://cookbook.openai.com/examples/fine_tuning_for_function_calling) for more information.

[

Fine-tuning for function calling

Learn how to fine-tune a model for function calling

](https://cookbook.openai.com/examples/fine_tuning_for_function_calling)