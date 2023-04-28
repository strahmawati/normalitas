import streamlit as st

def main():
    st.title('Normality Calculator')
    
    # Input parameters
    volume = st.number_input('Volume of Solution (mL)', min_value=0.01, step=0.01, value=100.0)
    mol_equivalent = st.number_input('Number of Mol Equivalents', min_value=0.01, step=0.01, value=1.0)
    
    # Calculate normality
    normality = mol_equivalent / (volume / 1000)
    
    # Show result
    st.write(f'Normality = {normality:.4f} N')

if __name__ == '__main__':
    main()
