import React from 'react';
import {Image, StyleSheet, Text, View} from 'react-native';
import {Button} from '../components/Button';
import {CommonActions, useNavigation} from '@react-navigation/native';

export const Index = () => {
  const navigation = useNavigation();
  return (
    <View style={style.contenedor}>
      <Text style={style.bienvenido}>BIENVENIDO</Text>
      <Image
        style={style.img}
        source={{
          uri: 'https://www.cronista.com/tools/image.php?id=427324&p=/files/image/427/427324/61f4c02f3338a.jpg&w=810&h=456&s=3f182dfe1ea28efdb6c804483959edd8',
        }}
      />

      <View style={style.colorcito}>
        <Button
          title="Ingrese"
          onPress={() =>
            navigation.dispatch(CommonActions.navigate({name: 'DIVISIÓN'}))
          }
        />
      </View>
    </View>
  );
};
const style = StyleSheet.create({
  contenedor: {
    backgroundColor: 'white',
    justifyContent: 'center',
    padding: 10,
    flex: 1,
  },
  bienvenido: {
    color: 'black',
    fontWeight: 'bold',
    fontSize: 14,
  },
  img: {
    height: 150,
    width: 250,
  },
  colorcito:{
    backgroundColor:'#ffdadd'
  }
});
