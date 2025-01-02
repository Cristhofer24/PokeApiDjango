import React from 'react';
import {StyleSheet, Text, TouchableOpacity} from 'react-native';

interface ButtonProps {
  title: string;
  onPress: () => void;}

export const Button = ({title, onPress}: ButtonProps) => {
  return (
    <TouchableOpacity style={styles.boton} onPress={onPress}>
      <Text style={styles.text3}>{title}</Text>
    </TouchableOpacity>
  );
};
const styles = StyleSheet.create({
  text3: {
    textAlign: 'center',
    fontWeight: 'bold',
    color: 'white',
    fontSize: 20,
  },
  boton: {
    backgroundColor: '#7368f5',
    borderRadius: 15,
    padding: 5,
    paddingVertical: 10,
    marginBottom: 10,
  },
});
