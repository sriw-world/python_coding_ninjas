Length of LL

def length(head) :
    #Your code goes here
    ctr = 0
    while head is not None:
        ctr = ctr+1
        head = head.next
    return ctr
    
Print ith node

def printIthNode(head, i):
    ctr = 0
    while head:
        if i == ctr:
            print(head.data)
            break
        ctr+=1
        head = head.next
    return
    
Delete node
