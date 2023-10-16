# gen.py

import os
import sys
import shutil

def copy_template_file(directory_path, behavior_name, destination_path=None):
    template_file = behavior_name
    source_file_path = os.path.join(directory_path, template_file)
    
    # 파일이 존재하는지 확인합니다.
    if os.path.exists(source_file_path):
        if not destination_path:
            destination_path = os.getcwd()
        
        # 목적지 경로를 지정합니다.
        dest_file_path = os.path.join(destination_path, template_file)
        
        # 파일을 복사합니다.
        shutil.copy2(source_file_path, dest_file_path)
        print(f"{template_file} has been copied to {destination_path}.")
    else:
        print(f"{template_file} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the behavior name as an argument.\nusage : python gen.py [template name]")
        sys.exit(1)
    
    behavior_name = sys.argv[1]
    copy_template_file('./DTEMPBUILDER/src/behavior_templates', behavior_name)
