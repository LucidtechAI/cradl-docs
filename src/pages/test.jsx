import React from 'react';
import Layout from '@theme/Layout';

import Card from '../components/card/Card';
import Container from '../components/card/Container';
import Lead from '../components/Lead';

import mockupVid from '@site/static/img/m.jpeg';


//import Card from "../src/components/card/Card"
//import Container from "../src/components/card/Container"
//import Lead from "../src/components/Lead"

export default function Hello() {
  return (
    <Layout title="Hello" description="Hello React Page">
      <div
        style={{
          // display: 'flex',
          // justifyContent: 'center',
          // alignItems: 'center',
          // height: '50vh',
          // fontSize: '20px',
          marginTop: '30px auto 0 auto',
          maxWidth: '100%'
        }}>
        <div
        style={{
          margin: '30px auto 0 auto',
          maxWidth: '80%'
        }}>

            <h1>Create New Model</h1>
            <img src={mockupVid} />
            <div className='w-full h-8'></div>
            <Lead text="Evverybody is the exception, which some convoluted way of doing things." />

            {/* <Container>
                <Card header="STEP-BY-STEP GUIDE" title="One or multiple AI models?" description="«My documents look very different. Will I need to pay for multiple models?»"/>
                <Card header="STEP-BY-STEP GUIDE" title="A complete beginner's guide to ANNOTATING training data." description="Getting the most out of your model by mastering data annotation."/>
                <Card header="Kategori" title="Overskrift" description="Ingress"/>
            </Container>

            <Container>
                <Card header="CUSTOMER CASE" title="EQUINOR - Norway's largest energy company." description="How Equinor is automating data flows with CRADL."/>
                <Card header="CUSTOMER CASE" title="DNB - Parsing ." description="How Scandinavia's largest bank is using CRADL for their customers."/>
            </Container> */}
            </div>

        {/* <p>
          Edit <code>pages/helloReact.js</code> and save to reload!
        </p> */}
      </div>
    </Layout>
  );
}