def quickSort(head):
    if not head or not head.next:
        return head

    pivot = head.data
    less = None
    equal = None
    greater = None

    curr = head

    while curr:
        next_node = curr.next

        if curr.data < pivot:
            curr.next = less
            less = curr
        elif curr.data == pivot:
            curr.next = equal
            equal = curr
        else:
            curr.next = greater
            greater = curr

        curr = next_node

    less = quickSort(less)
    greater = quickSort(greater)

    result = None
    tail = None

    for part in (less, equal, greater):
        if part:
            if result is None:
                result = part
            else:
                tail.next = part

            tail = part
            while tail.next:
                tail = tail.next

    return result
