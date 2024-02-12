import React, {useState} from 'react';
import {StyleSheet, Text, View, TextInput} from 'react-native';
import {Button} from '../components/Button';

export const Dividir = () => {
  const [nume1, setNumero1] = useState<string>('');
  const [nume2, setNumero2] = useState<string>('');
  const [res, setRes] = useState<number | null>(null);
  const [resultado, setResultados] = useState<string>('');
  const Divi = (nume1: number, nume2: number): number | string => {
    if (nume1 === 0 && nume2 === 0) { return 'Indeterminación.';
    } else if (nume2 === 0 || nume1 === 0) { return 'No hay número divisible para cero.';
    } else { return nume1 / nume2;
    }
  };

  const calculo = () => {
    if (nume1 !== '' && nume2 !== '') {
      const numu = parseFloat(nume1);
      const numd = parseFloat(nume2);

      if (!isNaN(numu) && !isNaN(numd)) {
        const division = Divi(numu, numd);
        if (typeof division === 'string') {
          setResultados(division);
          setRes(null);
        } else {
          setRes(division);
          setResultados('');
        }
      } else {
        setResultados('Ingrese números válidos.');
        setRes(null);
      }
    }
  };
  return (
    <View style={styles.contenedor1}>
      <Text>Formulario División </Text>

<Text style={styles.ingrese}>Ingrese el primer número</Text>
      <TextInput 
        style={styles.text2}
        value={nume1}
        onChangeText={text => setNumero1(text)}
        keyboardType="numeric"
      />
<Text style={styles.ingrese}>Ingrese el segundo número</Text>
      <TextInput
        style={styles.text2}
        value={nume2}
        onChangeText={text => setNumero2(text)}
        keyboardType="numeric"
      />

      <View style={styles.divi}>
        {res !== null && !isNaN(res) && (
          <Text>La división es= {resultado}</Text>
        )}
        {resultado === null && <Text>El resultado=</Text>}
        {resultado && <Text>{resultado}</Text>}
        <Button title="Dividir" onPress={calculo}/>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  text2: {
    borderColor: '#040404',
    margin: 15,
    height: 50,
    borderWidth: 3,
    padding: 10,
  },

  divi: {
    alignItems: 'center',
    width: '110%',
    marginTop: 40,
    padding: 20,
color:' #070707 '
  },
  contenedor1: {
    alignItems: 'center',
    padding: 10,
    flex: 10,
  },

  ingrese:{
    top:10,
    padding:20,
    color:'black',
    textAlign:'center'
    , justifyContent:'center'
  }
});
