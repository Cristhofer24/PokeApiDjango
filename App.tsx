import 'react-native-gesture-handler';
import React from 'react';
import {StackNavigation} from './src/navigation/StackNavigator';
import {NavigationContainer} from '@react-navigation/native';

const App = () => {
  return (
    <NavigationContainer>
      <StackNavigation />
    </NavigationContainer>
  );
};
export default App;
