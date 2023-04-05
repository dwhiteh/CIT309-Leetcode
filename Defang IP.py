class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = address.defang(".")
        defanging = "[.]"
        done = defanging.join(defang)
        return done


