# RAISIM, A PHYSICS ENGINE FOR ROBOTICS AND AI RESEARCH (v1.10)

Click to watch the video

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/CN0ah5-OWik/0.jpg)](https://www.youtube.com/watch?v=CN0ah5-OWik)


Documentation available on the [RaiSim Tech website](http://raisim.com).

## License

You should get a valid license and an activation key from the [RaiSim Tech website](http://raisim.com) to use RaiSim.
Post issues to this github repo for questions. 
Send an email to info.raisim@gmail.com for any special inquiry.

## Supported OS

MAC (including m1), Linux, Windows.


## Build

1. Create the build folder
```
mkdir build && cd build
```

2. Create the CMakeList file
```
cmake .. -DCMAKE_INSTALL_PREFIX=/home/steven/RL_ws/src/raisimlib/build -DRAISIM_EXAMPLE=ON -DRAISIM_PY=ON -DPYTHON_EXECUTABLE=$(python3 -c "import sys; print(sys.executable)")
```

3. Build the RaiSim package
```
make install -j4
```

4. Export the path
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/steven/RL_ws/src/raisimlib/build/lib
export PYTHONPATH=$PYTHONPATH:/home/steven/RL_ws/src/raisimlib/build/lib
```

5. Build the RaisimGymTorch package in raisimGymTorch folder
```
sudo python3 setup.py develop
```

## Usage

1. Launch the Unity simulator in /raisimlib/raisimUnity/linux
```
./raisimUnity.x86_64
```

2. Launch the training file
```
python raisimGymTorch/env/envs/rsg_anymal/runner.py
```

3. If want to output the log, use this command instead
```
python runner.py | tee output.log
```

4. Replay the trained the model
```
python3 tester.py --weight /home/roahm/RL_ws/src/raisimlib/raisimGymTorch/data/anymal_locomotion/2022-03-07-13-17-11/full_3400.pt
```

5. Retrain the model
```
python3 runner.py
```

## Comparison note
1. Change the file path in Environment.hpp to change the map, then compile the code. Use the tester.py to check the performance
```
sudo python3 setup.py develop
```

The list of the map included in the file is shown below:
- heightMap_1.txt: 15-by-15 flat terrain (all 0.4)
- heightMap_2.txt: 15-by-15 training terrain (0 - 0.5)
- heightMap_3.txt: 15-by-15 testing terrain (0 - 0.5)
- heightMap_4.txt: 15-by-15 challenging terrain (0 - 0.75)
- heightMap_5.txt: 15-by-15 impossible terrain (0 - 1.0)
- heightMap_11.txt: 30-by-30 flat terrain (all 0.4)
- heightMap_12.txt: 30-by-30 training terrain (0 - 0.5)
- heightMap_13.txt: 30-by-30 testing terrain (0 - 0.5)
- heightMap_14.txt: 30-by-30 challenging terrain (0 - 0.75)
- heightMap_15.txt: 30-by-30 impossible terrain (0 - 1.0)

2. Instead of the preset random map, can also use terrain generator to create a map in Environment.hpp. The robot needs to contact the ground to start the training.

3. Robot model can be switched in Environment.hpp file.

4. RL_training.txt shows the training history data for poster and final report of ECE545. The saved training weights are located in ./raisimGymTorch/saved_data.

## Useful Scripts
1. Generate the random map using txt file
```
python map_generator.py
```

2. Plot the training history
```
python plot_train_history.py
```

3. Plot the average reward history
```
python plot_reward_history.py
```
