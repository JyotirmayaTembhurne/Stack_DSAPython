class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students.count(sandwiches[0]):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
            if len(students) == 0:
                break
        return len(students)
