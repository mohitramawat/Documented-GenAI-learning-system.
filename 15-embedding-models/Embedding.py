from sentence_transformers import SentenceTransformer

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample text (chunk) that we want to convert into vector embeddings
Chunk = '''
Welcome to Shri L.D. Ramawat Travels. Our buses run daily from Jodhpur to various locations.
The luggage limit is 15kg per passenger. Extra luggage costs ₹100 per kg.
Refunds are only processed if cancelled 24 hours before the departure time.
'''

# encode() converts text into numerical vector representation
vector = model.encode(Chunk)

# Print generated embedding vector
print(vector)

# Print total dimensions/length of the vector
# This tells how many numerical values are present in the embedding
print(len(vector))