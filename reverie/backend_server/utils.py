# Select the GPT4All Model you'll use for the simulation. See: https://observablehq.com/@simonw/gpt4all-models
gpt4all_model="orca-mini-3b.ggmlv3.q4_0.bin"
max_tokens = 30
temperature = 0.5

# Put your name
key_owner = "Zihan Pan"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose
debug = False