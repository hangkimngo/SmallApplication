# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    next_id=1
    def __init__(self, description, name, workload):
        self.description = description
        self.programmer = name
        self.workload = workload
        self.finished = "NOT FINISHED"
        self.id= Task.next_id
        Task.next_id +=1
    def is_finished(self):
        return self.finished == "FINISHED"
    
    def mark_finished(self):
        self.finished = "FINISHED"
    
    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}"

class OrderBook:
    def __init__(self):
        self.orderbook=[]
        self.programmerlist=set()
    
    def add_order(self,description,name,workload):
        book=Task(description,name, workload)
        self.orderbook.append(book)
        if book.programmer not in self.programmerlist:
            self.programmerlist.add(book.programmer) 

    def all_orders(self):
        return self.orderbook
    
    def programmers(self):
        return list(self.programmerlist)
    
    def mark_finished(self, id:int):
        for book in self.orderbook:
            if book.id == id:
                book.mark_finished()
                return
        raise ValueError("no matching task")

    def finished_orders(self):
        return [book  for book in self.orderbook if book.is_finished()  ]
    
    def unfinished_orders(self):
        return [book for book in self.orderbook if not book.is_finished()]

    def status_of_programmer(self, programmer:str):
        if programmer not in self.programmers():
            raise ValueError("no programmer with the given name")

        finished_books= self.finished_orders()
        unfinished_books= self.unfinished_orders()
        finished= len([book for book in finished_books if book.programmer == programmer])
        unfinised= len([book for book in unfinished_books if book.programmer == programmer])
        finished_hr= sum([book.workload for book in finished_books if book.programmer == programmer])
        unfinished_hr = sum([book.workload for book in unfinished_books if book.programmer == programmer])
        return (finished, unfinised, finished_hr,unfinished_hr)

class OrderBookApplication:
    def __init__(self) -> None:
        self.__orderbook = OrderBook()

    def help(self):
        print("commands:") 
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks") 
        print("3 list unfinished tasks") 
        print("4 mark task as finished") 
        print("5 programmers") 
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                description=input("description: ")
                try:
                    name_workload=input("programmer and workload estimate: ").split()
                    programmer=name_workload[0]
                    workload=int(name_workload[1])
                    self.__orderbook.add_order(description, programmer,workload)
                    print("added!")
                except:
                    print("erroneous input")
            elif command == "2":
                finished=self.__orderbook.finished_orders()
                if len(finished) == 0:
                    print("no finished tasks")
                else:
                    print( "\n".join([str(book) for book in finished]))
            elif command == "3":
               
                unfinished=self.__orderbook.unfinished_orders()
                if  len(unfinished) == 0:
                    print("no unfinished tasks")
                else:
                    print( "\n".join([str(book) for book in unfinished]))
            elif command == "4":
                id=input("id: ")
                try:
                    self.__orderbook.mark_finished(int(id))
                    print("marked as finished")
                except:
                    print("erroneous input")
            elif command == "5":
                print( "\n".join([programmer for programmer in self.__orderbook.programmers() ]))
            elif command == "6":
                name = input("programmer: ")
                try:
                    status= self.__orderbook.status_of_programmer(name)
                    print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
                except:
                    print("erroneous input")
application = OrderBookApplication()
application.execute()
