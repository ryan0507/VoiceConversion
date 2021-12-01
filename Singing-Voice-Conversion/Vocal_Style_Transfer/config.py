# Epoch Parameter
n_epochs = 3000
checkpoint_every = 100

# Preprocessing Hyper parameter (Don't need when we preprocess with Spleeter)
sr = 16000  # sampling rate
n_features = 24  # Mceps coefficient
frame_period = 5.0  # n_frames 128 is about 0.5 sec
n_frames = 512  # fixed-length segment randomly
num_mcep = 24  # n_features랑 같은듯

# Model Hyper parameter
began = True  # True : Cycle-BeGan, False : CycleGan
# Cycle beGAN
g_type = "gated_cnn"  # or "u_net"
mini_batch_size = 1  # mini_batch_size = 1 is better
generator_learning_rate = 0.0002
generator_learning_rate_decay = generator_learning_rate / 200000
discriminator_learning_rate = 0.0001
discriminator_learning_rate_decay = discriminator_learning_rate / 200000
lambda_cycle = 10
lambda_identity = 5

# CycleGAN Hyper parameter
generator_lr = 0.0002
generator_lr_decay = generator_lr / 200000
discriminator_lr = 0.0001
discriminator_lr_decay = discriminator_lr / 200000
cycle_lambda = 10
identity_lambda = 5

# Additional BEGAN parameter
gamma_A = 0.5
gamma_B = 0.5
lambda_k_A = 0.001
lambda_k_B = 0.001
balance_A = 0
balance_B = 0
# kta Initial Value
k_t_A = 0
k_t_B = 0

# Data & Model Path
dataset_A = "./data/train/A"
dataset_B = "./data/train/B"
test_dir = "./data/test"
direction = "B2A"  # or "B2A"
log_dir = "./log"
model_dir = "./model"
