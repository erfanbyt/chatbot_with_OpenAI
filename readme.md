# Chatbot project!

This repository contains the mini-project I did to develop a chatbots open OpenAI!

The content of the chat is stored inside a Redis memory running in a docker container. Below is the instructions on how to run this program on your local machine. 

**Step 1**: First make sure you have API key to use OpenAI. Create your keys and store them inside `.env` file in your project directory.
```bash
OPENAI_API_KEY=<your API key>
```

**Step 2**: Create the docker container for running Redis locally, if you don't have Redis installed in your machine!

```bash 
docker pull redis/redis-stack
```

```bash 
docker run --name redis-container -p 6379:6379 -d -v <your project direcotry>:/data  redis/redis-stack
```

**Step 3**
Once you your Redis container is up and running, run `main.py` and start chatting and enjoy!


Because Redis is keeping track of your chat with the LLM model, the LLM model will reply back to your question based on the information it has from you!

The example of running the model is shown below:
```
>>>>hello
Hello! How can I assist you today?
>>>>my name is Erfan and I live in Vancouver.
Nice to meet you, Erfan! Vancouver is a beautiful city. How do you like living there?
>>>>Can you tell me what my name is?
Yes, your name is Erfan. How can I assist you further?
>>>>where do I live?
You mentioned that you live in Vancouver. Is there something specific you'd like to know about the city or any other topic?
>>>>Tell me the best places I can visit in vancouver over the weekend?
Vancouver offers a variety of attractions and activities to enjoy over the weekend. Here are some popular places you might consider visiting:

1. **Stanley Park**: A must-visit for its stunning views, walking and biking trails, and the famous Seawall. Don’t miss the Totem Poles and the Vancouver Aquarium.

2. **Granville Island**: This vibrant area features a public market, artisan shops, galleries, and restaurants. Try some delicious local food, and enjoy the scenic waterfront views.

3. **Capilano Suspension Bridge Park**: Experience the breathtaking views from the suspension bridge and explore the surrounding rainforest and treetop walkways.

4. **Grouse Mountain**: If you enjoy outdoor activities, head to Grouse Mountain for hiking, zip-lining, or skiing in the winter. The Skyride offers panoramic views of the city and mountains.

5. **Gastown**: Vancouver's historic district, known for its charming cobblestone streets, unique shops, restaurants, and the iconic Gastown Steam Clock.

6. **English Bay Beach**: Relax by the waterfront, enjoy sunbathing or take a stroll along the beach. It’s a great spot for people-watching and enjoying sunset views.

7. **Museum of Anthropology**: Located at UBC, this museum showcases indigenous art and cultural artifacts, offering insight into the rich history of the First Nations.

8. **VanDusen Botanical Garden**: A beautiful garden with diverse plant collections, walking paths, and stunning landscapes that provide a peaceful escape in the city.

9. **Lynn Canyon Park**: A lesser-known alternative to Capilano, Lynn Canyon features beautiful trails, waterfalls, and a suspension bridge in a natural setting.

10. **The Vancouver Art Gallery**: If you appreciate art, check out this gallery for an impressive collection of works, including pieces by Canadian artists.

Whether you're in the mood for nature, culture, or some great food, Vancouver has something for everyone to enjoy over the weekend!
>>>>Thanks for your recommendations!
You're welcome! I'm glad you found them helpful. If you have any more questions or need further suggestions, feel free to ask. Enjoy your weekend in Vancouver!


```