with open('output_list.txt', 'r') as file:
    lines = [line.rstrip() for line in file.readlines()][1:]

print('.. list-table::')
print('   :header-rows: 1')
print('')
print('   * - Index')
print('     - Redshift')
print('     - Output type')

for i, line in enumerate(lines):
    z, output_type = line.split(', ')
    print(f'   * - {i}')
    print(f'     - {z[:5]}')
    print(f'     - {output_type}')
