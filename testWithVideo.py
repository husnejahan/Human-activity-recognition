import torch
import numpy as np
from network import C3D_model
import cv2
torch.backends.cudnn.benchmark = True

def CenterCrop(frame, size):
    h, w = np.shape(frame)[0:2]
    th, tw = size
    x1 = int(round((w - tw) / 2.))
    y1 = int(round((h - th) / 2.))

    frame = frame[y1:y1 + th, x1:x1 + tw, :]
    return np.array(frame).astype(np.uint8)


def center_crop(frame):
    frame = frame[8:120, 30:142, :]
    return np.array(frame).astype(np.uint8)


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Device being used:", device)

    with open('/Users/mosthusnejahan/Desktop/project_most/dataloaders/labels.txt', 'r') as f:
        class_names = f.readlines()
        f.close()
    # init model
    model = C3D_model.C3D(num_classes=4)
    checkpoint = torch.load('run/run_1/models/C3D-kth_dataset_epoch-99.pth.tar', map_location=lambda storage, loc: storage)
    model.load_state_dict(checkpoint['state_dict'])
    model.to(device)
    model.train()

    # read video
    video = 'person02_handclapping_d3_uncomp.avi' # insert test video file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('outputVideo.avi',fourcc, 10.0, (160,120))
    
    cap = cv2.VideoCapture(video)
    retaining = True
    # vid_writer = cv2.VideoWriter('videos/output_{}.avi'.format('vid'),cv2.VideoWriter_fourcc('M','J','P','G'), 10, (171, 128))
    clip = []
    while retaining:
        retaining, frame = cap.read()
        # print(frame.shape)
        if not retaining and frame is None:
            continue
        tmp_ = center_crop(cv2.resize(frame, (171, 128)))
        tmp = tmp_ - np.array([[[90.0, 98.0, 102.0]]])
        clip.append(tmp)
        if len(clip) == 16:
            inputs = np.array(clip).astype(np.float32)
            inputs = np.expand_dims(inputs, axis=0)
            inputs = np.transpose(inputs, (0, 4, 1, 2, 3))
            inputs = torch.from_numpy(inputs)
            inputs = torch.autograd.Variable(inputs, requires_grad=False).to(device)
            with torch.no_grad():
                outputs = model.forward(inputs)

            probs = torch.nn.Softmax(dim=1)(outputs)
            label = torch.max(probs, 1)[1].detach().cpu().numpy()[0]
            print("label {} ".format(class_names[label]))

            cv2.putText(frame, class_names[label].split(' ')[-1].strip(), (20, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 0, 255), 1)
            cv2.putText(frame, "prob: %.4f" % probs[0][label], (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 0, 255), 1)
            clip.pop(0)
        out.write(frame)
        cv2.imshow('result', frame)
    out.release()
    #     vid_writer.write(frame)
    # vid_writer.release()
        # cv2.waitKey(30)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
