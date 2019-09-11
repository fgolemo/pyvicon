from pyvicon.pyvicon import PyVicon, StreamMode, Result
import numpy as np


class Tracker(object):

    def __init__(self, ipport, object_names):
        assert type(object_names) == type([])  # check for list
        super().__init__()
        self.object_names = object_names

        self.picon = PyVicon()
        # print("SDK version : {}".format(test.__version__))
        # print("frame", test.get_frame())
        res = self.picon.connect(ipport)
        if res != Result.Success:
            print("Couldn't connect to Vicon:", res)

        res = self.picon.set_stream_mode(StreamMode.ClientPull)
        if res != Result.Success:
            print("Couldn't set stream mode:", res)

        self.picon.get_frame()  # need this for start

        res = self.picon.enable_marker_data()
        if res != Result.Success:
            print("Couldn't enable marker data:", res)

        self.picon.get_frame()  # need this for start

        self.marker_count = {}
        self.markers = {}
        for obj in object_names:

            self.marker_count[obj] = self.picon.get_marker_count(obj)
            if self.marker_count[obj] == 0:
                print(f"Couldn't find object '{obj}'")

            self.markers[obj] = []
            for i in range(self.marker_count[obj]):
                self.markers[obj].append(self.picon.get_marker_name(obj, i))

        print("Markers:")
        print(self.markers)

    def _get_frame(self):
        for i in range(10):
            res = self.picon.get_frame()
            if res == Result.Success:
                break
        if res != Result.Success:
            return False
        return True

    def get_pos(self, obj, marker_idx=None, new_frame=True):
        if new_frame:
            # try and get a frame, retry if necessary
            if not self._get_frame():
                return None

        if marker_idx is not None:
            assert type(marker_idx) == type(3)  # test int
            return self.picon.get_marker_global_translation(
                obj, self.markers[obj][marker_idx])

        else:
            out = []
            for m in self.markers[obj]:
                ans = self.picon.get_marker_global_translation(obj, m)
                if ans is not None:
                    out.append(ans)
            return np.array(out)

    def get_multi_pos(self, objs):
        if not self._get_frame():
            return None

        out = {}
        for o in objs:
            out[o] = self.get_pos(o, new_frame=False)
        return out

    def get_dist(self, objs):
        assert len(objs) == 2
        res = self.get_multi_pos(objs)
        mean_a = np.mean(res[objs[0]], axis=0)
        mean_b = np.mean(res[objs[1]], axis=0)

        if np.isnan(mean_a).any() or np.isnan(mean_b).any():
            return None
        # print(mean_a, mean_b)

        return np.linalg.norm(mean_a - mean_b)
