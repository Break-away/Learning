
class LNode:
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

class LListunderflow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head = None
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
    def is_empty(self):
        return self._head is None
    def pop(self):
        if self._head is None:
            return LListunderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
    def pop_last(self):
        if self._head is None:
            return LListunderflow('{0} is empty'.format(__name__))
        e = self._head
        if e.next is None:
            self._head = None
        while e.next.next is not None:
            e = e.next
        p = e.next
        e.next = None
        return p
    def findall(self):
        p = self._head
        while p is not None:
            print('elem:', p.elem, end=' ')
            if p.next is not None:
                print(p.next, end='')
            p = p.next
            print('')
        if p is None:
            return "nothin to return"
    def pred(args):
            pass
    def find(self, elem):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next
    def proc(args):
        psss
    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next
    def elements(self):
        """生成器遍历"""
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next
    def insert(self, n, elem):
        p = self._head
        if n == 0:
            self.prepend(elem)
        else:
            i = 0
            while i < n-2 and p.next is not None:
                p = p.next
                i = i + 1
            if p.next is not None:
                next = p.next
                node = LNode(elem)
                p.next, node.next = node, p.next
            elif p.next is None and i == n-2:
                self.append(elem)
            else:
                raise LListunderflow("%s is out of index" % n)
    def delete(self, elem):
        p = self._head
        if p.elem == elem:
            self.pop()
            return
        while p.next is not None:
            if p.next.elem == int(elem):
                if p.next.next is not None:
                    p.next = p.next.next
                    return
                else:
                    self.pop_last()
                    return
            p = p.next
        raise LListunderflow('{0} is not in elements'.format(elem))
    def reverse_llist(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p
    def sort1(self):
        if self._head is None:
            return None
        p = self._head
        while p.next is not None:
            c = self._head
            pc = p.next
            while pc.elem <= c.elem:
                p.next = self._head
                self._head = p
                break
            while pc.elem > c.elem:
                cp = c
                c = c.next
            pc.next = c
            cp.next = pc
            p = p.next










class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head =  LNode(elem, self._head)
    def append(self, elem):
        p = self._head
        if p is None:
            self.prepend(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
    def pop_last(self):
        if self._head is None:
            raise LListunderflow
        p = self._head
        if p.next is None:
            self._head = None
            self._rear = None
        while p.next.next is not None:
            p = p.next
        p.next = None
        self._rear = p

class DLNode(LNode):
    def __init__(self, elem, prev=None, _next=None):
        LNode.__init__(self, elem, _next)
        self.prev = prev

class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)
    def prepend(self, elem):
        node = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = node
            self._head = node
        else:
            node.next.prev = node
            self._head = node
    def append(self, elem):
        node = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = node
            self._rear = node
        else:
            node.pre.next = node
            self._rear = node
    def pop(self):
        if self._head is None:
            raise LListunderflow
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        else:
            self._rear = None
    def pop_last(self):
        if self._rear is None:
            raise LListunderflow
        self._rear = self._rear.prev
        if self._rear is not None:
            self._rear.next = None
        else:
            self._head = None




"""test"""
# llist = LList1()
# for i in range(10):
#     llist.prepend(i)
# for m in range(10, 20):
#     llist.append(m)
#
# llist.delete(19)
# # llist.findall()
# for n in llist.filter(lambda x: x % 2 == 0):
#     print(n)

dllist = DLList()
print(dllist.findall())
dllist.prepend(1)
dllist.prepend(1)
print(dllist.findall())
print(dllist._head)
print(dllist._rear)
dllist.pop()
print(dllist._head)
print(dllist._rear)
print(dllist.is_empty())

