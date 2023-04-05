class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = address.split(".")
        defanging = "[.]"
        done = defanging.join(defang)
        return done


