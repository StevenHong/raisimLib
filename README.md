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
