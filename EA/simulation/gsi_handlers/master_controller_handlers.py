from sims4.gsi.schema import GsiGridSchema
    sub_schema.add_field('tag', label='Tag', width=0.25)
    sub_schema.add_field('sim', label='Sim', width=0.15)
    sub_schema.add_field('log', label='log')
    sub_schema.add_field('sim', label='ID', width=0.2)
    sub_schema.add_field('work_entry', label='Work')
    sub_schema.add_field('sim', label='ID', width=0.2)
    sub_schema.add_field('work_entry', label='Work')
def archive_master_controller_entry(entry):
    archiver.archive(data=entry)
