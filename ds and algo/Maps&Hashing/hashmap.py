'''The class diagram for HashMaps would look something like this.'''

class HashMap:
    def __init__(self):
        self.num_entries = 0
    
    def put(self,key,value):
        pass

    def get(self,key):
        pass

    def size(self,size):
        return self.num_entries
    

'''Can we use arrays to store key-value pairs?

We can certainly use one array to store the names of the students and 
use another array to store their corresponding heights at the corresponding 
indices.

What will be the time complexity in this scenario?

To obtain height of a student, say Potter, Harry, we will have to traverse the 
entire array and check if the value at a particular index matches Potter, Harry.
 Once we find the index in which this value is stored, we can use this index to 
 obtain the height from the second array.

Thus, because of this traveral, complexity for get() operation becomes $O(n)$.
 Even if we maintain a sorted array, the operation will not take less than 
 $O(log(n))$ complexity.

What happens if a student leaves a class? We will have to delete the entry 
corresponding to the student from both the arrays.

This would require another traversal to find the index. And then we will have to
 shift our entire array to fill this gap. Again, the time complexity of operation
  becomes $O(n)$'''

'''Is it possible to use linked lists for this problem?

We can certainly modify our LinkedListNode to have two 
different value attributes - one for name of the student and the other for height.

But we again face the same problem. In the worst case, 
we will have to traverse the entire linked list to find the height of a 
particular student.
 Once again, the cost of operation becomes $O(n)$.'''


''''Simply put, hash functions are these really incredible magic 
functions which can map data of any size to a fixed size data. 
This fixed sized data is often called hash code or hash digest.'''


'''For a given string, say abcd, 
a very simple hash function can be sum of corresponding ASCII values.'''
def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    
    return hash_code

hashcode1 = hash_function('abcd')
print(hashcode1)



'''Looks like our hash function is working fine. But is this really a good hash function?

For starters, it will return the same value for abcd and bcda. Do we want that? We can create 24 different permutations for the string abcd and each will have the same value. We cannot put 24 values to one index.

Obviously, this makes it clear that our hash function must return unique values for unique objects.

When two different inputs produce the same output, then we have something called a collision. An ideal hash function must be immune from producing collisions.

Let's think something else.

Can product help? We will again run in the same problem.

The honest answer is that we have differernt hash functions for different types of keys. The hash function for integers will be different from the hash function for strings, which again, will be different for some object of a class that you created.

However, let's try to continue with our problem and try to come up with a hash function for strings.'''


'''
Hash Function for Strings
For a string, say abcde, a very effective function is treating this as number of prime number base p. Let's elaborate this statement.

For a number, say 578, we can represent this number in base 10 number system as$$5*10^2 + 7*10^1 + 8*10^0$$

Similarly, we can treat abcde as$$a * p^4 + b * p^3 + c * p^2 + d * p^1 + e * p^0$$

Here, we replace each character with its corresponding ASCII value.

A lot of research goes into figuring out good hash functions and this hash function is one of the most popular functions used for strings. We use prime numbers because the provide a good distribution. The most common prime numbers used for this function are 31 and 37.

Thus, using this algorithm, we can get a corresponding integer value for each string key and store it in the array.

Note that the array used for this purpose is called a bucket array. It is not a special array. We simply choose to give a special name to arrays for this purpose. Each entry in this bucket array is called a bucket and the index in which we store a bucket is called bucket index.'''



class HashMap1:
    def __init__(self,initial_size = 0):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p  =37
        self.num_entries = 0
    
    def put(self, key,value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self,key):
        return self.get_hash_code(key)
    
    def get_hash_code(self,key):
        key = str(key)
        #num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character)*current_coefficient
            current_coefficient *= self.p
            current_coefficient = current_coefficient
        
        return hash_code
    
hashmap1 = HashMap1()
bucket_index = hashmap1.get_bucket_index('abcd')
print(bucket_index)



'''Compression Function
We now have a good hash function which will return unique values for unique objects. But let's look at the values. These are huge. We cannot create such large arrays. So we use another function - compression function to compress these values so as to create arrays of reasonable sizes.

A very simple, good, and effective compression function can be mod len(array). The modulo operator % returns the remainder of one number when divided by other.

So, if we have an array of size 10, we can be sure that modulo of any number with 10 will be less than 10, allowing it to fit into our bucket array.

Because of how modulo operator works, instead of creating a new function, we can write the logic for compression function in our get_hash_code() function itself.'''



class HashMap33:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient

        return hash_code % num_buckets                                # one last compression before returning
    
    
    def size(self):
        return self.num_entries


'''Collision Handling
As discussed earlier, when two different inputs produce the same output, then we have a collision. Our implementation of get_hash_code() function is satisfactory. However, because we are using compression function, we are prone to collisions.

Consider the following scenario.

We have a bucket array of length 10 and we get two different hash codes for two different inputs, say 355, and 1095. Even though the hash codes are different in this case, the bucket index will be same because of the way we have implemented our compression function. Such scenarios where multiple entries want to go to the same bucket are very common. So, we introduce some logic to handle collisions.

There are two popular ways in which we handle collisions.

Closed Addressing or Separate chaining
Open Addressing

Closed addressing is a clever technique where we use the same bucket to store multiple objects. The bucket in this case will store a linked list of key-value pairs. Every bucket has it's own separate chain of linked list nodes.

In open addressing, we do the following:

If, after getting the bucket index, the bucket is empty, we store the object in that particular bucket

If the bucket is not empty, we find an alternate bucket index by using another function which modifies the current hash code to give a new code

Separate chaining is a simple and effective technique to handle collisions and that is what we discuss here.

Implement the put and get function using the idea of separate chaining.'''



class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap4:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient

        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries