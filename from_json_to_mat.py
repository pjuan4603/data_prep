import json
import numpy as np
import scipy
from scipy import io

def generate_matlab_mixed_data(data_str, data_type, course_num, quiz_only = False):
    """
    generate the matlab data for our baseline method bptf
    :return:
    """
    for fold in range(1, 2):
        TTr = []
        TTe = []
        with open('data.json', 'rb') as f:
            data = json.load(f)
            num_users = data['num_users']
            num_questions = data['num_quizs']
            num_attempts = data['num_attempts']
            if quiz_only:
                num_discussions = 0
            else:
                num_discussions = data['num_disicussions']
            size = np.array([[num_users, num_questions + num_discussions, num_attempts]])
            mat_dict = {}
            subs = []
            vals = []
            # print(np.array(data['train']))
            for (student, question, obs, attempt, resource) in data['train']:
                if int(resource) == 0:
                    subs.append([student + 1, question + 1, attempt + 1])
                    vals.append([obs])
                else:
                    subs.append([student + 1, num_questions + question + 1, attempt + 1])
                    vals.append([obs])
            train_set = (subs, vals, size)
            dt = np.dtype([('subs', 'O'), ('vals', 'O'), ('size', 'O')])
            TTr = np.array([[train_set]], dtype=dt)
            name = 'train{}'.format(fold)
            mat_dict[name] = TTr
            scipy.io.savemat('TTr.mat'.format(data_str, data_type, course_num, fold), mat_dict)
            mat_dict = {}
            mat_q_dict = {}
            mat_e_dict = {}
            subs = []
            subs_q = []
            subs_e = []
            vals = []
            vals_q = []
            vals_e = []
            for (student, question, obs, attempt, resource) in data['test']:
                subs.append([student + 1, question + 1, attempt + 1])
                vals.append([obs])
                if resource == 0:
                    subs_q.append([student + 1, question + 1, attempt + 1])
                    vals_q.append([obs])
                elif resource == 1:
                    subs_e.append([student + 1, num_questions + question + 1, attempt + 1])
                    vals_e.append([obs])
                else:
                    raise SystemError("HAHA")
            test_set = (subs, vals, size)
            dt = np.dtype([('subs', 'O'), ('vals', 'O'), ('size', 'O')])
            TTe = np.array([[test_set]], dtype=dt)
            name = 'test{}'.format(fold)
            mat_dict[name] = TTe
            scipy.io.savemat('TTe.mat'.format(data_str, data_type, course_num, fold), mat_dict)
            test_set = (subs_q, vals_q, size)
            dt = np.dtype([('subs', 'O'), ('vals', 'O'), ('size', 'O')])
            TTe = np.array([[test_set]], dtype=dt)
            name = 'test{}q'.format(fold)
            mat_q_dict[name] = TTe
            scipy.io.savemat('TTeq.mat'.format(data_str,data_type, course_num, fold), mat_q_dict)
            #
            # test_set = (subs_e, vals_e, size)
            # dt = np.dtype([('subs', 'O'), ('vals', 'O'), ('size', 'O')])
            # TTe = np.array([[test_set]], dtype=dt)
            # name = 'test{}e'.format(fold)
            # mat_e_dict[name] = TTe
            # scipy.io.savemat('data/{}/{}/matlab_mixed/test{}e.mat'.format(data_str, course_num, fold), mat_e_dict)
        # print(np.array(mat['TTr'][0][0][0]).shape)
        # print(np.array(mat['TTr'][0][0][1]).shape)
        # print(np.array(mat['TTr'][0][0][2]).shape)
def prepare_simulation():
    data_str = 'simulated_data'
    # data_type = 'Quiz_Discussion_STQ'
    # data_type = 'Quiz_Only_Discussion_STQ'
    data_type = 'Quiz_Discussion_STQ_Thresholded'
    course_num = ''
    if 'Quiz_Only' in data_type:
        quiz_only = True
    else:
        quiz_only = False
    generate_matlab_mixed_data(data_str, data_type, course_num, quiz_only)


def main():
    prepare_simulation()


main()