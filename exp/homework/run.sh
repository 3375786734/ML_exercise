g++ -g LBP.cpp `pkg-config --cflags  --libs  opencv` -o LBP 
./LBP
python SVM_material_reco.py
rm LBP
