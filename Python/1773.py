class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        sum = 0
        file= []
        for item in items:
            if ruleKey == "type":
                file.append(item[0])
            elif ruleKey == "color":
                file.append(item[1])
            elif ruleKey == "name":
                file.append(item[2])
        for i in file:
            if i == ruleValue:
                sum += 1
        return sum