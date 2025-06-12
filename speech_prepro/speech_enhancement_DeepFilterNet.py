import os
import sys
# 获取项目根目录（假设脚本在 speech_prepro/ 下）
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from DeepFilterNet.DeepFilterNet.df.enhance  import enhance, init_df, load_audio, save_audio
from DeepFilterNet.DeepFilterNet.df.utils import download_file
import time

if __name__ == "__main__":
    # Load default model
    model, df_state, _, _ = init_df()
    # audio, _ = load_audio("noisy_snr0.wav", sr=df_state.sr())
    audio, _ = load_audio("/Bspace/xionglizhu/henan/step2/speech_prepro/samples/16k/dialogue.wav", sr=df_state.sr())
    # Denoise the audio
    time_start = time.time()
    enhanced_audio = enhance(model, df_state, audio)
    time_end = time.time()
    # Save for listening
    execution_time = time_end - time_start
    print(f"执行时间: {execution_time:.3f} 秒")
    save_audio("tes_enhanced.wav", enhanced_audio, df_state.sr(), output_dir = "/Bspace/xionglizhu/henan/step2/speech_prepro/output/dialogue")
