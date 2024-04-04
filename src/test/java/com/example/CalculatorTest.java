package com.example;

import junit.framework.TestCase;

public class CalculatorTest extends TestCase {

    private final Calculator calculator = new Calculator();
    public void testAdd() {
        System.out.println("Running testAdd");
        assertEquals(5, calculator.add(2, 3));
    }

    public void testSubtract() {
        System.out.println("Running testSubtract");
        assertEquals(1, calculator.subtract(3, 2));
    }
}