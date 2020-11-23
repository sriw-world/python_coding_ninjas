https://www.programiz.com/dsa/huffman-coding
https://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

Huffman Coding -- text compression algo


BCAADDDCCACACAC
Each character occupies 8 bits. There are a total of 15 characters in the above string. Thus, a total of 8 * 15 = 120 bits are required to send this string.

Using the Huffman Coding technique, we can compress the string to a smaller size.

Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.

Once the data is encoded, it has to be decoded. Decoding is done using the same tree.


1. Calculate the frequency of each character in the string.
2. Sort the characters in increasing order of the frequency. These are stored in a priority queue Q.
3.Make each unique character as a leaf node.
4. Create an empty node z. Assign the minimum frequency to the left child of z and assign the second minimum frequency to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.
5.Remove these two minimum frequencies from Q and add the sum into the list of frequencies (* denote the internal nodes in the figure above).
6.Insert node z into the tree.
7. Repeat steps 3 to 5 for all the characters.
8. For each non-leaf node, assign 0 to the left edge and 1 to the right edge.

For sending the above string over a network, we have to send the tree as well as the above compressed-code. The total size is given by the table below.

 

Character	Frequency	Code	Size
A	          5	      11	  5*2 = 10
B	        1	       100	  1*3 = 3
C	                  6	  0  	6*1 = 6
D	3	101	3*3 = 9
4 * 8 = 32 bits	15 bits	 	28 bits
 

Without encoding, the total size of the string was 120 bits. After encoding the size is reduced to 32 + 15 + 28 = 75.


Huffman Coding Algorithm
create a priority queue Q consisting of each unique character.
sort then in ascending order of their frequencies.
for all the unique characters:
    create a newNode
    extract minimum value from Q and assign it to leftChild of newNode
    extract minimum value from Q and assign it to rightChild of newNode
    calculate the sum of these two minimum values and assign it to the value of newNode
    insert this newNode into the tree
return rootNode


import heapq

class BinaryTreeNode:
  def __init__(self,value,freq):
    self.value=value
    self.freq=freq
    self.left=None
    self.right=None
  def __it__(self,other):
    return self.frequency<other.freq
  
  def __eq__(self,other):
    return self.frequency == other.freq
    
class HuffmannCoding:
  def __init__(self,path):
    self.path=path
    self.__heap=[]
    self.__codes={}
  def _make_frequency_dict(self,text):
    freq_dict={}
    for char in text:
      if char not in freq_dict:
        freq_dict=[char]=0
      freq_dict=[char] +=1
    return freq_dict
    
  def __buildHeap(self,freq_dict):
    for key in freq_dict:
      frequency = freq_dict[key]
      binary_tree_node = BinaryTreeNode(key,frequency)
      heapq.heappush(self.__heap,binary_tree_node)
    
  def __buildTree(self):
    while(len(self.__heap)>1):
    ##pop min 2 node
			   binary_tree_node_1 = heapq.heappop(self.__heap)
			   binary_tree_node_2 = heapq.heappop(self.__heap)
     ##node with sum freq
			   merged = BinaryTreeNode(None, binary_tree_node_1.freq + binary_tree_node_1.freq)
			   merged.left = binary_tree_node_1
			   merged.right = binary_tree_node_2

			   heapq.heappush(self.__heap, merged)
    return
    
  
  def __buildCodesHelper(self, root, current_code):
    if(root == None):
     return

    if(root.value != None):
     self.__codes[root.value] = current_code
     ###self.reverse_mapping[current_code] = root.char
     return
###add 0 to left 1 to righ
    self.__buildCodesHelper(root.left, current_code + "0")
    self.__buildCodesHelper(root.right, current_code + "1")


	def __buildCodes(self):
 #TREE WITH FREQ has been build 
		root = heapq.heappop(self.__heap)
		current_code = ""
		self.make_codes_helper(root, current_code)
  
  
  def __getEncodedText(self, text):
    encoded_text = ""
    for character in text:
      encoded_text += self.__codes[character]
    return encoded_text
    
   def __getPaddedEncodedText(self, encoded_text):
      extra_padding = 8 - len(encoded_text) % 8
      for i in range(extra_padding):
	 encoded_text += "0"

      padded_info = "{0:08b}".format(extra_padding)
      encoded_text = padded_info + encoded_text
      return encoded_text
      
  def __getByteArray(self, padded_encoded_text):
    #if(len(padded_encoded_text) % 8 != 0):
     # print("Encoded text not padded properly")
     # exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
      byte = padded_encoded_text[i:i+8]
      b.append(int(byte, 2))
    return b

  
  def compress(self):
  
    filename, file_extension = os.path.splitext(self.path)
    output_path = filename + ".bin"
   # text="dsfdsfdsgdsgdsdafsf"
    with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
    	   text = file.read()
	   text = text.rstrip()

	    ##make freq
	    freq_dict = self._make_frequency_dict(text)

	    ##contruct heap from freq dict
	    self.__buildHeap(freq_dict)

	    ##contruct binaary tree from heap 
	    self.__buildTree()
	    ##contruct codes from binaary tree 
	    self.__buildCodes()
	    ##create encoded text from codes
	    encoded_text = self.__getEncodedText(text)
	    ##put encoded text into binary file


	    ###pad encoded text
	    padded_encoded_text = self.__getPaddedEncodedText(encoded_text)
	    bytes_array = self.__getByteArray(padded_encoded_text)

	    #return this binary file as output
	    final_bytes = bytes(bytes_array)
	    output.write(final_bytes)
    return output    
    
    
