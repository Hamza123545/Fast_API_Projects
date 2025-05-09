import httpx
import asyncio

async def get_chatbot_response(user_message: str, user_id: str):
    url = "http://127.0.0.1:8000/chat/"
    
    payload = {
        "user_id": user_id,
        "text": user_message,
        "metadata": {
            "timestamp": "2025-05-09T12:00:00Z",
            "session_id": "1234-5678-91011"  # Example session_id
        },
        "tags": ["chatbot", "greeting"]  # Optional tags
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        
    if response.status_code == 200:
        return response.json()["reply"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
async def main():
    user_id = "user_1"
    user_message = "Hello, chatbot!"
    reply = await get_chatbot_response(user_message, user_id)
    print("Chatbot Response:", reply)

# Run the main function
asyncio.run(main())
