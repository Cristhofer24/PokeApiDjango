import {Index} from '../screens/Index';
import {Dividir} from '../screens/Dividir';
import {createStackNavigator} from '@react-navigation/stack';
import {StyleSheet} from 'react-native';

export type RootStackParamList = {
  Index: undefined;
  Dividir: undefined;
};

const Stack = createStackNavigator<RootStackParamList>();
export const StackNavigation = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="Index"
        component={{title: 'Pagina1'}}
        options={Index}
      />
      <Stack.Screen
        name="Dividir"
        components={{title: 'Pagina2'}}
        options={Dividir}
      />
    </Stack.Navigator>
  );
};

const style = StyleSheet.create({
  color12: {
    backgroundColor: '#fcb0fc',
    padding: 5,
  },
});
