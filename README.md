# projekt_Kowalski_Juliusz_Kowalski_Kacper
Projekt z przedmiotu NiOdSR
# ROS 2 Camera Subscriber & Robot Control

Paczka ROS 2 Humble przeznaczona do sterowania robotem mobilnym (TurtleBot3) za pomocą gestów myszy na obrazie z kamery (OpenCV).

## Autorzy
* Juliusz Kowalski
* Kacper Kowalski

## Funkcjonalności
1. **Camera Node**: Subskrypcja i wyświetlanie obrazu z kamery.
2. **Mouse Interaction**: Rysowanie na obrazie i publikacja punktów kliknięcia.
3. **Robot Control**: Sterowanie robotem na podstawie strefy kliknięcia:
   * **Górna połowa ekranu**: Jazda do przodu.
   * **Dolna połowa ekranu**: Jazda do tyłu.

## Wymagania
* ROS 2 Humble
* Python 3
* Pakiety ROS: `geometry_msgs`, `sensor_msgs`, `cv_bridge`
* Biblioteka: `opencv-python`
* Symulator: `turtlebot3_gazebo`

## Instalacja

1. Przejdź do katalogu `src` w swoim workspace:
   cd ~/ros2_ws/src
2. Zainstaluj brakujące zależności (opcjonalnie):
  rosdep install --from-paths src --ignore-src -r -y
3. Przejdź do folderu:
   cd ~/ros2_ws/src/camera_subscriber/camera_subscriber
4. Stwórz plik:
   robot_control.py
5. Edytuj w folderze cd ~/ros2_ws/src/camera_subscriber/ plik setup.py:
     entry_points={
        'console_scripts': [
   robot_control = camera_subscriber.robot_control:main',
   ]
    },
6. Ponownie przejdź do katalogu `src` w swoim workspace:
   cd ~/ros2_ws/src
7. Zbuduj paczkę:
  colcon build --packages-select camera_subscriber
8. Załaduj środowisko:
  source install/setup.bash
9. Uruchom:
ros2 run camera_subscriber robot_control
