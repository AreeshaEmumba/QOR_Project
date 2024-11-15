'''
# Open the log file and output file
with open('/home/emumba/Desktop/Designs/9871/logs/optimization/dummy_logfile.txt', 'r') as log_file, open('/home/emumba/Desktop/9871/qor/fermi.txt', 'w') as output_file:
    for line in log_file:
        # Check if the line contains "stat = value" pattern
        if '=' in line:
            # Split the line by '=' and strip any extra spaces
            stat, value = map(str.strip, line.split('=', 1))
            # Write to output file in the format "stat : value"
            output_file.write(f"{stat} : {value}\n")

print("fermi.txt file has been generated with the desired format.")
'''

import argparse
import os
import shutil

"""
def parse_log_file(log_file_path, output_file_path):
    with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
        for line in log_file:
            # Check if the line contains "stat = value" pattern
            if '=' in line:
                # Split the line by '=' and strip any extra spaces
                stat, value = map(str.strip, line.split('=', 1))
                # Write to output file in the format "stat : value"
                output_file.write(f"{stat} : {value}\n")
    print(f"fermi.txt file has been generated at {output_file_path}.")
"""

def parse_log_file(log_file_path, output_file_path):
    # Define categories for the stats based on the key names
    # Main Stats category
    main_stats_keys = [
        'fermi_id', 'checker_id', 'gpu', 'expect_run_time_50_gpu', 'expect_run_time_1_gpu', 
        'user', 'name', 'max_err_per_partion', 'total_errors', 'design_size', 'mask_file_size', 
        'machine_name', 'run_date_time', 'revision_branch', 'revision_commit', 'revision_date', 
        'fermi_job_name', 'tmod_name', 'process_condition', 'partition', 'grid', 
        'optimizer_iterations', 'force_flag', 'force_screenshot', 'mpi_retry_count', 
        'num_qtm3_iterations', 'num_qtm4_iterations', 'num_qtm5_iterations', 'mask_num_deleted_shapes', 
        'mask_num_upsized_shapes', 'num_pixel_corrections', 'num_part_corrections', 
        'delete_mask_polygon_count', 'delete_mask_polygon_max', 'delete_mask_polygon_min', 
        'upsizing_mask_polygon_count', 'upsizing_mask_polygon_max', 'upsizing_mask_polygon_min', 
        'number_of_optimized_partitions', 'total_number_of_partitions', 'parsing_time'
    ]

    # Runtime Analysis Stats category
    runtime_analysis_stats_keys = [
        'target_prep_runtime', 'ctm_fg', 'qtm_fg', 'ctm_prep', 'qtm0_prep', 'qtm1_prep', 
        'qtm2_prep', 'qtm3_prep', 'qtm4_prep', 'qtm5_prep', 'qtm0_total', 'qtm1_total', 
        'qtm2_total', 'qtm3_total', 'qtm4_total', 'qtm5_total', 'ctm_exec_time', 'qtm_exec_time', 
        'postprocess_exec_time', 'total_fermi_runtime', 'the_checker_runtime'
    ]

    # Geometric Analysis Stats (Fermi) category
    geometric_analysis_stats_keys = [
        'mrc_area_count', 'mrc_area_max_value', 'mrc_area_min_value', 'mrc_area_marker_x', 
        'mrc_area_marker_y', 'imrcfix_max_correction_max_value', 
        'imrcfix_total_number_of_fixed_mrc_width_errors_count', 
        'imrcfix_total_number_of_partially_fixed_mrc_width_errors_count', 
        'imrcfix_the_worst_width_error_overall_max_value', 
        'imrcfix_total_number_of_fixed_mrc_spacing_errors_count', 
        'imrcfix_total_number_of_partially_fixed_mrc_spacing_errors_count', 
        'imrcfix_the_worst_spacing_error_overall_max_value', 
        'imrcfix_total_number_of_unimproved_mrc_errors_count', 
        'high_curvature_internal_checking_setting', 
        'high_curvature_external_checking_setting', 'mrc_area_setting', 'mrc_spacing_setting', 
        'mrc_width_setting', 'mrc_width_count', 'mrc_width_max_value', 'mrc_width_min_value', 
        'mrc_width_marker_x', 'mrc_width_marker_y', 'mrc_spacing_count', 'mrc_spacing_max_value', 
        'mrc_spacing_min_value', 'mrc_spacing_marker_x', 'mrc_spacing_marker_y', 
        'high_curvature_internal_checking_count', 'high_curvature_internal_checking_max_value', 
        'high_curvature_internal_checking_min_value', 'high_curvature_internal_checking_marker_x', 
        'high_curvature_internal_checking_marker_y', 'high_curvature_external_checking_count', 
        'high_curvature_external_checking_max_value', 'high_curvature_external_checking_min_value', 
        'high_curvature_external_checking_marker_x', 'high_curvature_external_checking_marker_y', 
        'xor_error_of_nominal_contour_greater_than_10_count', 
        'xor_error_of_nominal_contour_greater_than_10_max_value', 
        'xor_error_of_nominal_contour_greater_than_10_min_value', 
        'xor_error_of_nominal_contour_greater_than_10_marker_x', 
        'xor_error_of_nominal_contour_greater_than_10_marker_y', 
        'xor_error_of_negative_dose_greater_than_10_count', 
        'xor_error_of_negative_dose_greater_than_10_max_value', 
        'xor_error_of_negative_dose_greater_than_10_min_value', 
        'xor_error_of_negative_dose_greater_than_10_marker_x', 
        'xor_error_of_negative_dose_greater_than_10_marker_y', 
        'xor_error_of_positive_dose_greater_than_10_count', 
        'xor_error_of_positive_dose_greater_than_10_max_value', 
        'xor_error_of_positive_dose_greater_than_10_min_value', 
        'xor_error_of_positive_dose_greater_than_10_marker_x', 
        'xor_error_of_positive_dose_greater_than_10_marker_y', 
        'xor_error_of_negative_defocus_greater_than_10_count', 
        'xor_error_of_negative_defocus_greater_than_10_max_value', 
        'xor_error_of_negative_defocus_greater_than_10_min_value', 
        'xor_error_of_negative_defocus_greater_than_10_marker_x', 
        'xor_error_of_negative_defocus_greater_than_10_marker_y', 
        'xor_error_of_positive_defocus_greater_than_10_count', 
        'xor_error_of_positive_defocus_greater_than_10_max_value', 
        'xor_error_of_positive_defocus_greater_than_10_min_value', 
        'xor_error_of_positive_defocus_greater_than_10_marker_x', 
        'xor_error_of_positive_defocus_greater_than_10_marker_y'
    ]

    # Statistical Analysis category (multiple subcategories)
    statistical_analysis_keys = {
        'EPE_Target_vs_Mask_Simulation_Negfocus': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi'],
        'EPE_Target_vs_Mask_Simulation_Negdose': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi'],
        'EPE_Target_vs_Nominal_Mask_Simulation_f0d0': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi'],
        'EPE_Target_vs_Mask_Simulation_Posfocus': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi'],
        'EPE_Target_vs_Mask_Simulation_Posdose': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi'],
        'Width_of_PV_Band_by_Dose': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi'],
        'Width_of_PV_Band_by_Focus': ['mean_fermi', 'std_fermi', 'max_fermi', 'count_fermi', 'marker_x_fermi', 'marker_y_fermi']
    }

    # Initialize dictionaries to hold categorized stats
    main_stats = {}
    runtime_analysis_stats = {}
    geometric_analysis_stats = {}
    statistical_analysis = {key: {} for key in statistical_analysis_keys}
    leftover_stats = {}

    # Read the log file and categorize the stats
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if '=' in line:
                # Split the line by '=' and strip any extra spaces
                stat, value = map(str.strip, line.split('=', 1))

                # Categorize the stat based on the predefined keys
                if stat in main_stats_keys:
                    main_stats[stat] = value
                elif stat in runtime_analysis_stats_keys:
                    runtime_analysis_stats[stat] = value
                elif stat in geometric_analysis_stats_keys:
                    geometric_analysis_stats[stat] = value
                elif any(stat in sublist for sublist in statistical_analysis_keys.values()):
                    for subcategory, keys in statistical_analysis_keys.items():
                        if stat in keys:
                            statistical_analysis[subcategory][stat] = value
                else:
                    leftover_stats[stat] = value
    # Write the categorized stats to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write('[Main Stats]\n')
        for stat, value in main_stats.items():
            output_file.write(f'{stat}: {value}\n')

        output_file.write('\n[Runtime Analysis Stats]\n')
        for stat, value in runtime_analysis_stats.items():
            output_file.write(f'{stat}: {value}\n')

        output_file.write('\n[Geometric Analysis Stats]\n')
        for stat, value in geometric_analysis_stats.items():
            output_file.write(f'{stat}: {value}\n')

        for subcategory, stats in statistical_analysis.items():
            output_file.write(f'\n[Statistical Analysis:{subcategory}]\n')
            for stat, value in stats.items():
                output_file.write(f'{stat}: {value}\n')


def copy_qor_folder(jobid_folder, rsync_directory):
    qor_folder = os.path.join(jobid_folder, 'qor')
    if os.path.exists(qor_folder):
        # Define the destination path to include both jobid folder and qor folder
        destination = os.path.join(rsync_directory, os.path.basename(jobid_folder), 'qor')
        # Copy the qor folder (including the folder itself) to the destination
        shutil.copytree(qor_folder, destination, dirs_exist_ok=True)
        print(f"Copied QOR folder to {destination}.")
    else:
        print(f"QOR folder does not exist in {jobid_folder}.")

def main():
    parser = argparse.ArgumentParser(description="Process log files and manage job directories.")
    parser.add_argument('-l', '--location', required=True, help="Path to the directory containing jobid folders.")
    parser.add_argument('-id', '--jobid', required=True, help="ID of the job (jobid folder name).")
    parser.add_argument('-p', '--parse', action='store_true', required=True, help="Parse the log file and save as fermi.txt in qor folder.")
    parser.add_argument('-r', '--rsync', action='store_true', help="Copy QOR folder to the default rsync directory.")

    args = parser.parse_args()

    # Hardcoded rsync directory path
    rsync_directory = '/home/emumba/Desktop/Rsync'  

    # Construct paths for the log file and fermi.txt output
    jobid_folder = os.path.join(args.location, args.jobid)
    log_file_path = os.path.join(jobid_folder, 'logs/optimization/dummy_logfile.txt')
    qor_output_folder = os.path.join(jobid_folder, 'qor')
    output_file_path = os.path.join(qor_output_folder, 'fermi.txt')

    # Parse the log file and save fermi.txt if -p is provided
    if args.parse:
        if not os.path.exists(log_file_path):
            print(f"Log file {log_file_path} not found.")
            return
        os.makedirs(qor_output_folder, exist_ok=True)
        parse_log_file(log_file_path, output_file_path)

    # Copy QOR folder to rsync directory if -r is provided
    if args.rsync:
        copy_qor_folder(jobid_folder, rsync_directory)

if __name__ == '__main__':
    main()