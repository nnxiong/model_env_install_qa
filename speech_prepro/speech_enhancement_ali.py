import time
import os
import sys
# 将ClearerVoice-Studio目录添加到Python路径
sys.path.append(os.path.abspath('/Bspace/henan/step2/ClearerVoice-Studio'))
from clearvoice import ClearVoice  # Import the ClearVoice class for speech processing tasks

# Initialize ClearVoice with time measurement
class SpeechEnhancer:
    def __init__(self):
        self.myClearVoice = ClearVoice(task='speech_enhancement', model_names=['MossFormer2_SE_48K'])
        # self.myClearVoice = ClearVoice(task='speech_enhancement', model_names=['MossFormer2_SE_48K','FRCRN_SE_16K'])

    def speech_enhancement(self, file: bool, input_speech: str, output_path: str):
        ## ----------------- Using a Single Model ----------------------
        start_process = time.time()
        if file:
            # 1st calling method: Process single file
            output_wav = self.myClearVoice(input_path=input_speech)
            self.myClearVoice.write(output_wav, output_path=output_path)
        else:
            # 2st calling method: Process dir
            self.myClearVoice(input_path=input_speech, online_write=True, output_path=output_path)
        
        write_time = time.time() - start_process
        print(f"File speech enhancement time: {write_time:.2f} seconds")


if __name__ == '__main__':
    # Process single file
    input_file = "/Bspace/xionglizhu/henan/step2/speech_prepro/samples/48k/dialogue.wav"
    # input_file = "/Bspace/xionglizhu/henan/step2/speech_prepro/samples/four_speakers_segment_001.wav"
    # input_file = "/Bspace/xionglizhu/henan/step2/speech_prepro/samples/four_speakers_segment_001.wav"
    output_dir = "/Bspace/xionglizhu/henan/step2/speech_prepro/output/dialogue/"
    os.makedirs(output_dir, exist_ok=True)
    # output_path = os.path.join(output_dir, "dialogue_enhanced_16k.wav")
    output_path = os.path.join(output_dir, "four_speakers_segment_001_MossFormer2_SE_48K.wav")
    enhancer = SpeechEnhancer()
    enhancer.speech_enhancement(True, input_file, output_path)

    # Process dir
    # input_file = "/Bspace/ASR_audio_data/raw_audio/语音转文字—语音原素材/cut/"
    # # input_file = "/Bspace/xionglizhu/henan/step2/speech_prepro/samples/four_speakers_segment_001.wav"
    # output_dir = "/Bspace/ASR_audio_data/raw_audio/语音转文字—语音原素材/cut_enhanced/"
    # os.makedirs(output_dir, exist_ok=True)
    # enhancer = SpeechEnhancer()
    # enhancer.speech_enhancement(False, input_file, output_dir)