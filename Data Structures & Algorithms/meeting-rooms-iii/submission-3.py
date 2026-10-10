import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #n rooms from 0 to n-1
        room_count = [[0, i] for i in range(n)] #index 0 is room 0, index n-1 is room n-1, first value is how many meetings been held in that room but make it negative so sorting can sort it min first
        meetings.sort() #sorted by the first item, the start time
        print(meetings)
        m_booked = [] #(end time, meeting room), each meeting room should only be in once
        free = [(i,0) for i in range(n)] #min heap for free rooms, when a room is free lowest one gets added, when a room gets popped from m_booked it should be added to free
        #when a room is popped from free it should be added to m_booked
        #dealyed end time = current end time + end time of the meeting that current meeting replaced
        heapq.heapify(free)
        heapq.heapify(m_booked)
        for m in meetings:
            s_time = m[0]
            e_time = m[1]
            if m_booked and s_time >= m_booked[0][0] or not free:
                found_yet = False
                while not found_yet and m_booked:
                    
                    finished_m = heapq.heappop(m_booked) #the meeting that sjstu finished, (time, room)
                    heapq.heappush(free, (finished_m[1], finished_m[0])) #now this room is free, push (room, end time)          
                    print(f"FOR FREE PUSHED {(finished_m[1], finished_m[0])}")
                    print(f"for meeting {m} top_availabel is {finished_m}")
                    if m_booked and m_booked[0][0] > s_time: #this means the next room is still booked
                        found_yet = True

            
            der_next = heapq.heappop(free) #next available room, (room, end time)
            der_room = der_next[0]
            der_end_time = der_next[1]
            if der_end_time > s_time: #that means this meeting had to wait for this room
                e_time += (der_end_time - s_time)
            heapq.heappush(m_booked, [e_time, der_room])
            print(f"meeting {m} went to {[e_time, der_room]}")
            room_count[der_room][0] -= 1

        print(sorted(room_count))
            
            



        return sorted(room_count)[0][1]


        