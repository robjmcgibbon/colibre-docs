import swiftsimio as sw

header = '''
  .. list-table::
   :header-rows: 1

   * - Index
     - Redshift
     - Age [Gyr]
     - Output type'''

print(header)

run_dir = '/cosma8/data/dp004/colibre/Runs/L0025N0188/Thermal'
for i in range(128):
    snap = sw.load(f'{run_dir}/snapshots/colibre_{i:04}/colibre_{i:04}.hdf5')
    output_type = snap.metadata.select_output
    z = snap.metadata.z
    age = snap.metadata.time.to_value('Gyr')

    print(f'   * - {i}')
    print(f'     - {z:.4f}')
    print(f'     - {age:.3f}')
    print(f'     - {output_type}')

    if i in [41, 84]:
        print(header)
