import numpy
def indicate(x,a):
        for i in xrange(7):
                if x==i:
                        a[i]=1
                        break
        if a[0]>0 and a[1]>0 and a[2]>0 and a[3]>0 and a[4]>0 and a[5]>0 and a[6]>0:
                return 1
        else:
                return 0
                
def number_of_times(x,n,a):
        for i in xrange(7):
                if x==i:
                        a[i]=a[i]+1
                        break
        return a
        

def prob(a):
        import numpy
        n=[0,1,2,3,4,5,6]
        return int(numpy.random.choice(n,1,p=a))
        

def swap(a):
        b = list(a)
        first_max = max(b)
        b.remove(first_max)
        second_max = max(b)
        b.remove(second_max)
        third_max = max(b)

        #get the minimums
        b = list(a)
        first_min = min(b)
        b.remove(first_min)
        second_min = min(b)
        b.remove(second_min)
        third_min = min(b)

        ## now swap 
        xMax, yMax, zMax = a.index(first_max), a.index(second_max), a.index(third_max)
        xMin, yMin, zMin = a.index(first_min), a.index(second_min), a.index(third_min)
        a[xMax], a[xMin] = a[xMin], a[xMax]
        a[yMax], a[yMin] = a[yMin], a[yMax]
        a[zMax], a[zMin] = a[zMin], a[zMax]
        return a
        

def toss():
        print "The rule of tossing is that you would choose even or odd, then you and your opponent would give an integer, if the sum of these two integers is as per your choice you win the toss"
        print "Even or Odd?"
        choice=raw_input()
        from random import randint
        comp_choice=randint(0,6)
        print "Enter an integer between 0 and 6"
        num_choice=int(raw_input())
        num=num_choice+comp_choice
        if choice=="Even":
                if num%2==0:
                        print "You won the toss"
                        print "Choose batting or bowling"
                        player_t_choice=raw_input()
                else:
                        print "You lost the toss"
                        t_choice=randint(1,2)
                        if t_choice==1:
                                print "Computer has chosen to bat"
                                player_t_choice="bowling"
                        else:
                                print "Computer has chosen to bowl"
                                player_t_choice="batting"
        else:
                if num%2==1:
                        print "You won the toss"
                        print "Choose batting or bowling"
                        player_t_choice=raw_input()
                else:
                        print "You lost the toss"
                        t_choice=randint(1,2)
                        if t_choice==1:
                                print "Computer has chosen to bat"
                                player_t_choice="bowling"
                        else:
                                print "Computer has chosen to bowl"
                                player_t_choice="batting"
                        
        return player_t_choice	

def no_of_wickets():
        print "How many wickets do you want?"
        for i in xrange(10):
                print i+1,
        print
        print "Please enter a response"
        no_wickets=int(raw_input())
        return no_wickets
        
def player_batting_first(wickets):
        runs=0
        count=0
        b=[0,0,0,0,0,0,0]
        a=[0,0,0,0,0,0,0]
        while wickets>0:
                count=count+1
                player_number=int(raw_input())
                number_of_times(player_number,count,a)
                c=[(float(x))/count for x in a]
                value=prob(c)
                if indicate(player_number,b)==0:
                        comp_response=randint(0,6)
                else:
                        comp_response=value
                print player_number,comp_response
                if player_number==comp_response:
                        print "Out"
                        wickets=wickets-1
                else:
                        runs=runs+player_number
        return runs
        
def player_batting_second(wickets,runs_by_comp):
        runs=0
        count=0
        b=[0,0,0,0,0,0,0]
        a=[0,0,0,0,0,0,0]
        while wickets>0:
                if runs>runs_by_comp:
                        return runs
                else:
                        count=count+1
                        player_number=int(raw_input())
                        number_of_times(player_number,count,a)
                        c=[(float(x))/count for x in a]
                        value=prob(c)
                        if indicate(player_number,b)==0:
                                comp_response=randint(0,6)
                        else:
                                comp_response=value	
                        print player_number,comp_response
                        if player_number==comp_response:
                                print "Out"
                                wickets=wickets-1
                        else:
                                runs=runs+player_number
        return runs
        
def player_bowling_first(wickets):
        runs=0
        count=0
        b=[0,0,0,0,0,0,0]
        a=[0,0,0,0,0,0,0]
        while wickets>0:
                count=count+1
                player_number=int(raw_input())
                number_of_times(player_number,count,a)
                c=[((float(x))/count) for x in a]
                c=swap(c)
                value=prob(c)
                if indicate(player_number,b)==0:
                        comp_response=randint(0,6)
                else:
                        comp_response=value	
                print player_number,comp_response
                if player_number==comp_response:
                        print "Out"
                        wickets=wickets-1
                else:
                        runs=runs+comp_response
        return runs
        
def player_bowling_second(wickets,runs_by_player):
        runs=0
        count=0
        b=[0,0,0,0,0,0,0]
        a=[0,0,0,0,0,0,0]
        while wickets>0:
                if runs>runs_by_player:
                        return runs
                else:
                        count=count+1
                        player_number=int(raw_input())
                        number_of_times(player_number,count,a)
                        c=[((float(x))/count) for x in a]
                        c=swap(c)
                        value=prob(c)
                        if indicate(player_number,b)==0:
                                comp_response=randint(0,6)
                        else:
                                comp_response=value	
                        print player_number,comp_response
                        if player_number==comp_response:
                                print "Out"
                                wickets=wickets-1
                        else:
                                runs=runs+comp_response
        return runs


from random import randint
number_of_wickets=no_of_wickets()
player_choice=toss()
if player_choice=="batting":
        runs_player=player_batting_first(number_of_wickets)
        print "You have scored", runs_player
        print "Computer needs to score",runs_player+1,"to win"
        runs_comp=player_bowling_second(number_of_wickets,runs_player)
        if runs_comp>runs_player:
                print "Computer scored:",runs_comp
                print "You Scored:",runs_player
                print "Computer Wins"
        elif runs_comp<runs_player:
                print "You scored",runs_player
                print "Computer scored",runs_comp
                print "You Win"
        else:
                print "Match Drawn"
else:
        runs_comp=player_bowling_first(number_of_wickets)
        print "Computer have scored", runs_comp
        print "You need to score",runs_comp+1,"to win"
        runs_player=player_batting_second(number_of_wickets,runs_comp)
        if runs_comp>runs_player:
                print "Computer scored:",runs_comp
                print "You Scored:",runs_player
                print "Computer Wins"
        elif runs_comp<runs_player:
                print "You scored",runs_player
                print "Computer scored",runs_comp
                print "You Win"
        else:
                print "Match Drawn"
import time
time.sleep(5)
        
                


