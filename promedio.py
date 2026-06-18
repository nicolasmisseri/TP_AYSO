#!/usr/bin/env python3
def compute_average(numbers):
	if not numbers:
		raise ValueError("La lista de números está vacía")
	return sum(numbers) / len(numbers)

def read_numbers_interactive():
	print("Ingrese números separados por espacios, o presione Enter para terminar:")
	s = input("> ").strip()
	if not s:
		return []
	parts = s.split()
	nums = []
	for p in parts:
		try:
			if "." in p:
				nums.append(float(p))
			else:
				nums.append(int(p))
		except ValueError:
			print(f"Ignorado: '{p}' no es un número válido")
	return nums

def main():
	nums = read_numbers_interactive()
	if not nums:
		print("No se ingresaron números. Saliendo.")
		return
	avg = compute_average(nums)
	print(f"Promedio: {avg}")

if __name__ == "__main__":
	main()
