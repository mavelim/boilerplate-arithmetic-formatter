# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


#print(arithmetic_arranger(["2 + 69", "45 + 635 ", "123 / 49","5 + 7","0 + hola"],"TRUE"))
print(arithmetic_arranger(['3801 - 2', '123 + 49'],True))




# Run unit tests automatically

main()
