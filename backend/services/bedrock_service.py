import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Create the Bedrock Runtime client
# boto3 automatically reads AWS_BEARER_TOKEN_BEDROCK from environment
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION", "ap-southeast-2"),
)


def generate_travel_recommendation(destination: str, days: int, budget: float, category: str) -> str:
    """
    Calls Amazon Bedrock (Nova Lite) via Converse API to generate
    a rich, structured daily travel itinerary.
    """
    prompt = f"""You are an expert travel planner. Create a detailed and structured {days}-day travel itinerary for {destination} with a total budget of ${budget:.2f} USD ({category} category).

For EACH day, you MUST include:

Morning (provide exactly 2-3 specific activities):
- Specific landmarks or attractions to visit
- Recommended breakfast spots or local food experiences
- Best time to visit to avoid crowds

Afternoon (focus on cultural sites and local experiences):
- Must-visit cultural sites, museums, or historical landmarks
- Authentic local experiences unique to {destination}
- Recommended lunch spots with local cuisine

Evening (include dinner spots and nightlife):
- Specific dinner restaurant recommendations with local specialties
- Evening entertainment or nightlife options
- Optional night market or scenic spots

Format the output clearly as:

Day X: [Theme for the day]

Morning:
- [activity 1]
- [activity 2]
- [activity 3]

Afternoon:
- [cultural site or experience 1]
- [cultural site or experience 2]

Evening:
- [dinner spot]
- [nightlife or entertainment]

Keep recommendations specific, practical, and within the {category} budget level.
Format your response as Markdown with headers (##) and bullet lists (-).
Make it exciting and memorable!"""

    response = client.converse(
        modelId=os.getenv("MODEL_ID", "amazon.nova-lite-v1:0"),
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    )

    ai_response = response["output"]["message"]["content"][0]["text"]
    return ai_response
