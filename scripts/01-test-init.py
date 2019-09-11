from pyvicon.pyvicon import PyVicon, StreamMode

test = PyVicon()
print("SDK version : {}".format(test.__version__))
print("frame",test.get_frame())
print(test.connect("192.168.10.102:801"))
print(test.set_stream_mode(StreamMode.ClientPull))
print("Connection status : {}".format(test.is_connected()))
# print(test.disconnect())
# print(test.start_server_multicast("localhost", "224.0.0.0"))
# print(test.connect_multicast("localhost", "224.0.0.0"))
# print(test.stop_server_multicast())
print("frame",test.get_frame())

# print (test.enable_device_data())
print (test.enable_marker_data())
# print (test.enable_unlabeled_marker_data())
# print (test.enable_segment_data())

print("frame",test.get_frame())

print ("frame no", test.get_frame_number())
print ("framerate", test.get_frame_rate())
print ("cam count",test.get_camera_count())

# print ("seg enabled", test.enab())
print ("dev enabled", test.is_device_data_enabled())
print ("marker enabled", test.is_marker_data_enabled())
print ("unlabl. marker enabled", test.is_unlabeled_marker_data_enabled())

print(test.get_axis_mapping())
print(test.get_subject_name(0))
print(test.get_marker_count("cube1"))
print(test.get_marker_name("cube1",0))
print(test.get_marker_name("cube1",1))
print(test.get_marker_name("cube1",2))
print (test.get_subject_root_segment_name("cube1"))
print("frame",test.get_frame())
print (test.get_segment_global_translation("cube1","cube11"))
# print (test.get)
print("frame",test.get_frame())

while True:
    test.get_frame()
    print (test.get_marker_global_translation("cube1","cube11"))
