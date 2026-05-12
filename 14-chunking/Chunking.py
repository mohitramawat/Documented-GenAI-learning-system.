from langchain_text_splitters import RecursiveCharacterTextSplitter

# Multi-line text using triple quotes (""" """)
# This text will be divided into smaller chunks
travel_policy_text = """
Welcome to Shri L.D. Ramawat Travels. Our buses run daily from Jodhpur to various locations.
The luggage limit is 15kg per passenger. Extra luggage costs ₹100 per kg.
Refunds are only processed if cancelled 24 hours before the departure time.
"""

# Creating an object of RecursiveCharacterTextSplitter
# chunk_size = Maximum number of characters in one chunk
# chunk_overlap = Number of overlapping characters between consecutive chunks
my_smart_splitter = RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=15,
)

# split_text() function splits the large text into smaller chunks
final_chunk = my_smart_splitter.split_text(travel_policy_text)

# Printing all chunks as a list
print(final_chunk)

print("\n------ Individual Chunks ------\n")

# enumerate() is used to get:
# 1. index  -> position number of the chunk
# 2. chunk  -> actual chunk text
#
# Python uses zero-based indexing:
# first index = 0
# second index = 1
#
# We use index + 1 so the output starts from Chunk 1 instead of Chunk 0
for index, chunk in enumerate(final_chunk):

    # f-string allows mixing variables directly inside text
    # Example:
    # f"Chunk Number {index + 1}"
    #
    # {index + 1} dynamically inserts the chunk number
    print(f"Chunk Number {index + 1}: {chunk}")